# GymBro: AI-Powered Fitness Assistant 🏋️‍♂️🤖

### Enhancing exercise posture through AI-driven assistance.

---

## 🔍 **Overview**
GymBro is a smart, virtual fitness assistant designed to help beginners perform exercises correctly. By leveraging cutting-edge deep learning and computer vision techniques, GymBro analyzes your posture and provides real-time feedback for improvement, making fitness more accessible and injury-free.

---

## 👥 **Meet the Team**
| Roll No.     | Team Member                  |  
|--------------|------------------------------|
| 210050043    | Desai Sai Pranav             |
|210050051    | Gangisetty Krishna Sai Kusal  |  
| 210050057    | Gorle Krishna Chaitanya      |  
| 210050103    |  Nagasai Saketh Naidu        |  

---

## 🚀 **Why GymBro?**
- 🌟 The fast-paced lifestyle and sedentary work culture lead to poor fitness levels.
- 🍔 Unhealthy eating habits combined with long commutes result in limited wellness time.
- 🏋️‍♀️ Many individuals lack access to physical trainers, leading to improper exercise techniques and injuries.
- 📊 **Fact:** A National Health and Nutrition Survey (Japan) highlights a 30% obesity rate in desk-job engineers — 10% higher than their non-engineer peers.

---

## 🌟 **Get Started**
1. Clone the repository:
   ```bash
   git clone https://github.com/YourRepo/GymBro.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the project
   ```bash
   python main.py


## 🔧 **Key Features**
1. **Real-Time Pose Estimation**:
   - Detects 17 key body points using the ultra-fast **MoveNet** model.
   - Calculates critical angles like shoulders, elbows, and wrists for posture analysis.
   - Optimized for real-time feedback.

2. **Trainer Key-Frame Extraction**:
   - Extracts key frames from trainer videos to benchmark correct postures.
   - Captures and saves critical angles as vectors for comparison.

3. **Dynamic Time Warping (DTW) & Optical Flow Tracking**:
   - Aligns user and trainer video frames, enabling accurate comparison despite timing differences.

4. **Affine Transformation**:
   - Aligns trainer and user frames into a common reference for consistent posture evaluation.

---

## 📚 **Technical Pipeline**

1. **Pose Estimation**
- Tracks essential key points (e.g., shoulders, elbows, hips, knees) using advanced models like OpenPose, MediaPipe, or HRNet.
- Extracts joint angles such as `Right Shoulder - Right Elbow - Right Wrist` using vector calculations for precise measurements.
- Incorporates confidence scores to prioritize high-reliability key-points and filters noisy data with temporal smoothing (e.g., Kalman filtering).

2. **Trainer Key-Frames**
- Captures and stores reference key-frames, representing ideal poses, with associated key points, angles, and optional annotations for motion dynamics.
- Stores key-frames in a structured format (e.g., JSON or database) to facilitate comparison and analysis.
- Automates key-frame extraction by clustering trainer motion data to identify critical transitions or peak movements.

3. **Dynamic Time Warping (DTW)**
- Matches user frames with trainer key-frames by comparing time-series data of joint angles or key-point positions.
- Handles variations in execution speed by aligning user movements to trainer motions dynamically.
- Optimized for real-time performance, ensuring feedback is delivered with minimal delay.

4. **Optical Flow Tracking**
- Tracks user’s motion at a pixel level to capture fine-grained movement details, complementing key-point tracking.
- Enhances movement matching accuracy by aligning dynamic motion patterns with trainer trajectories.
- Detects subtle shifts in posture or flow that may not be evident from key-points alone, ensuring holistic feedback.

5. **Affine Transformation**
- Applies transformations (scaling, rotation, translation) to align user and trainer poses to a unified reference frame.
- Normalizes variations in camera angle, user height, and limb proportions to ensure consistent analysis.
- Ensures robust posture alignment across diverse user profiles and setups, improving generalization.


---


## 🎯 **Results**
- **Posture Comparison:**
  - Clear visual differences between trainer (green) and user (red) are identified for correction.
- **Improvement Tracking:**
  - User feedback visually demonstrates posture improvement over attempts.
- Here a pic showing how to maintain a correct posture while doing a **PushUp**<br/>
  ![alt text](https://github.com/krishnachaitanya2004/GymBro/blob/main/results/final_res.png)


---
## 🔗 **References**
1. [GitHub Repo for output reference](https://github.com/NgoQuocBao1010/Exercise-Correction?tab=readme-ov-file)
2. [Paper Reference](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8856547&tag=1)
3. [Kaggle Model by Google](https://www.kaggle.com/models/google/movenet/tensorFlow2/singlepose-lightning/4?tfhub-redirect=true)
4. [Tensorflow Documentation](https://www.tensorflow.org/)
---

Hope you Enjoy the **Smarter Way** of being fit.

Made with ❤️ in Python 🐍




