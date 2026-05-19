#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class YoloDetectionNode(Node):
    def __init__(self):
        super().__init__('yolo_detection_node')
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')  

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',  # change to your actual camera topic
            self.image_callback,
            10
        )
        self.publisher = self.create_publisher(Image, '/yolo/detection_image', 10)
        self.get_logger().info('YOLO Detection Node started')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        results = self.model(frame, verbose=False)

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                if label == 'chair':
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'Chair {conf:.2f}',
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                                (0, 255, 0), 2)
                    self.get_logger().info(f'Chair detected! Confidence: {conf:.2f}')

        out_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)
    node = YoloDetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()