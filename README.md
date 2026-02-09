# 🤖 SEMANTIC SLAM

> A ROS2-based autonomous differential drive robot equipped with LiDAR for obstacle detection and navigation in Gazebo simulation.

---

## 📌 Table of Contents

- [📖 About](#-about)
- [🎯 Goals](#-goals)
- [✅ Progress Checkpoints](#-progress-checkpoints)
- [🛠️ Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [▶️ Usage](#️-usage)
- [📡 ROS2 Topics](#-ros2-topics)
- [📸 Demo / Results](#-demo--results)
- [🔮 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 📖 About

The **ROS2 LiDAR Bot** project focuses on building and simulating a mobile robot capable of:

- Perceiving its environment using LiDAR sensors  
- Publishing scan data in ROS2  
- Performing differential drive motion control  
- Enabling autonomous navigation using the Nav2 stack  

This project serves as both a learning platform and a foundation for real-world robotics deployment.

---

## 🎯 Goals

### Primary Objectives

- Build a working LiDAR-enabled robot simulation  
- Implement obstacle detection and avoidance  
- Integrate ROS2 Navigation (Nav2) for autonomous movement  

### Learning Outcomes

- Understanding ROS2 nodes, topics, TF frames  
- Working with URDF/Xacro robot models  
- Using Gazebo plugins for sensors and motion  
- Practicing SLAM + Path Planning pipelines  

---

## ✅ Progress Checkpoints

### Phase 1: Environment Setup

- [x] Create ROS2 workspace and repository  
- [x] Setup Gazebo Classic simulation environment  
- [x] Build differential drive base model  

---

### Phase 2: Robot Description (URDF/Xacro)

- [x] Add chassis and wheel links  
- [x] Configure joints properly  
- [ ] Improve inertial and collision properties  

---

### Phase 3: LiDAR Integration

- [x] Add LiDAR sensor in URDF  
- [ ] Verify `/scan` topic publishing  
- [ ] Tune sensor parameters for accuracy  

---

### Phase 4: Motion Control

- [x] Configure diff-drive Gazebo plugin  
- [ ] Publish velocity commands via `/cmd_vel`  
- [ ] Validate odometry output  

---

### Phase 5: Navigation & Autonomy

- [ ] Integrate SLAM Toolbox  
- [ ] Configure Nav2 stack  
- [ ] Achieve goal-to-goal autonomous navigation  

---

### Phase 6: Testing & Optimization

- [ ] Run obstacle avoidance benchmarks  
- [ ] Improve stability and localization  
- [ ] Add documentation + demo videos  

---

## 🛠️ Tech Stack

| Category        | Tools Used |
|----------------|------------|
| Framework       | ROS2 Humble |
| Simulation      | Gazebo Classic |
| Robot Model     | URDF / Xacro |
| Sensors         | LiDAR |
| Control         | Diff Drive Plugin |
| Navigation      | SLAM Toolbox + Nav2 (Planned) |
| Version Control | Git + GitHub |

---

## 📂 Project Structure

```bash
ros2_lidar_bot/
│── src/
│   └── lidar_bot_description/
│       ├── urdf/
│       ├── launch/
│       ├── config/
│       ├── worlds/
│       └── meshes/
│
│── README.md
│── package.xml
│── setup.py
