#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math


class LidarReader(Node):

    def __init__(self):
        super().__init__("lidar_reader")

        # Subscribe to LiDAR scan topic
        self.subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.scan_callback,
            10
        )

        self.get_logger().info("✅ LiDAR Reader Node Started!")

    def scan_callback(self, msg: LaserScan):

        ranges = msg.ranges
        n = len(ranges)

        # Helper function to ignore inf values
        def safe_min(data):
            filtered = [r for r in data if not math.isinf(r)]
            return min(filtered) if filtered else float("inf")

        # Indices for directions
        front_index = n // 2

        # Take small windows instead of single ray
        front = safe_min(ranges[front_index - 10: front_index + 10])
        left  = safe_min(ranges[-30:])
        right = safe_min(ranges[0:30])

        # Print distances
        self.get_logger().info(
            f"Front: {front:.2f} m | Left: {left:.2f} m | Right: {right:.2f} m"
        )

        # Simple obstacle warning
        if front < 0.5:
            self.get_logger().warn("🚨 Obstacle VERY close in front!")


def main(args=None):
    rclpy.init(args=args)

    node = LidarReader()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
