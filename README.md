# 🌟 GymBro: AI-Powered Exercise Posture Assistance 💪

![GymBro Logo](https://via.placeholder.com/800x200?text=GymBro+Logo)  
> *Your Virtual Fitness Trainer: Perfect Your Form Anytime, Anywhere!*  

---

## 🚀 Overview

**GymBro** is your personal AI gym assistant, designed to help fitness enthusiasts—especially beginners—achieve the perfect workout posture. Combining **Deep Learning** and **Computer Vision**, GymBro analyzes your form in real-time, offering actionable feedback to prevent injuries and optimize performance.

---

## 🔑 Key Features

### 🏋️ Pose Estimation
- **Model**: MoveNet (Lightning)  
- **Function**: Captures 17 key body points to calculate joint angles essential for posture evaluation.  
- **Why?** Real-time, ultra-fast analysis for seamless workout tracking.

---

### 🎞️ Trainer Key-frame Extraction
- **What?** Key angles from professionally executed exercises are vectorized from trainer videos.
- **How?** Automatically detects significant posture changes using L1-norm thresholds.

---

### 🌀 Dynamic Time Warping & Optical Flow
- **Why?** Accurately matches user and trainer frames, even with temporal differences.
- **Result?** Smooth real-time feedback.

---

### 🔄 Affine Transformation
- **Purpose**: Aligns user and trainer frames to a common reference frame.  
- **Magic?** Ensures consistent comparison with seamless matrix transformations.  

---

## 🛠️ Project Pipeline

1. **Pose Estimation**: Track key joints like shoulders, elbows, and knees.  
2. **Trainer Key-frame Extraction**: Identify and store key exercise frames.  
3. **Dynamic Time Warping & Optical Flow**: Compare user movement with trainer videos.  
4. **Affine Transformation**: Align frames for precise analysis.  

---

## 🎯 Problem Statement & Motivation

Modern life challenges fitness goals:  
⚠️ **Sedentary Work Culture**  
⚠️ **Limited Time**  
⚠️ **Lack of Personal Trainers**

### Did You Know?  
🚨 Engineers with desk jobs face a **30% obesity rate**, according to Japan's National Health and Nutrition Survey. That’s **10% higher** than their non-engineer peers!

---

## 🌈 Visual Results

📸 **Side-by-Side Comparison**  
Observe clear differences between your form and the trainer’s:  
- **Red Skeleton**: User  
- **Green Skeleton**: Trainer  

See your posture improve as you work out!

---

## 👥 Team Quad-eye

- **Gorle Krishna Chaitanya**  
- **Nagasai Saketh Naidu**  
- **Gangisetty Krishna Sai Kusal**  
- **Desai Sai Pranav**

---

## 📚 References

For in-depth exploration:  
- [Dynamic Time Warping Research](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8856547&tag=1)

---

## 🛠️ Getting Started

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/YourUsername/GymBro.git
cd GymBro
```

### 2️⃣ Install Dependencies  
Ensure Python 3.x is installed. Then run:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the App  
```bash
python main.py
```

### 4️⃣ Upload Videos  
Follow the prompts to upload your workout and get instant feedback.

---

## 🤝 Contributions Welcome!

Found a bug? Have a cool feature idea?  
Feel free to open an issue or submit a pull request. Let’s make fitness accessible for everyone!  

---

### 🌟 Star us on GitHub if you find this project helpful! 😊

![GitHub Stars](https://img.shields.io/github/stars/krishnachaitanya2004/GymBro?style=social)  
