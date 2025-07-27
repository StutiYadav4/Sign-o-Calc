# Sign-o-Calc
> A gesture-controlled calculator built using OpenCV, MediaPipe, and Python


## What is Sign-o-Calc?

**Sign-o-Calc** is a real-time, gesture-based calculator that lets you perform arithmetic operations — using just your hands! It uses your webcam to detect hand gestures and translates them into digits and mathematical operators to evaluate expressions on the go.

Whether you're doing math or just want to look cool while doing it, Sign-o-Calc is your sign language-powered math buddy 🤟

---

## ✨ Features

- 📸 Real-time webcam gesture detection using **OpenCV** and **MediaPipe**
- ✋ Detects all **digits (0–9)** using intuitive hand signs
- ➕➖✖️➗ Supports **+, -, *, /** operators
- 🟰 Use gestures for **equal** and **clear**
- 🚫 Shows **“Invalid Expression”** for consecutive operators
- 🧠 Clean output window with live expression updates

---

## 🧠 Gesture Mappings

| Gesture | Meaning | Fingers |
|--------|---------|---------|
| Fist | = | ✊ |
| Pinky | + | 🤙 |
| Thumb + Pinky | / | 🤙👉 |
| Index + Pinky | * | ✌️+Pinky |
| Index + Thumb + Pinky | - | 🤟+Pinky |
| Ring | Clear (C) | 💍 |
| Digits 0–9 | Shown Below | 👇 |

### ✋ Digit Mapping
| Digit | Gesture |
|-------|---------|
| 0 | Fist |
| 1 | Index |
| 2 | Index + Middle |
| 3 | Index + Middle + Ring |
| 4 | Index + Middle + Ring + Pinky |
| 5 | All Fingers |
| 6 | Thumb |
| 7 | Thumb + Index |
| 8 | Thumb + Index + Middle |
| 9 | Thumb + Index + Middle + Ring |

---

## 🚀 Demo

[![Sign-o-Calc Demo](https://img.youtube.com/vi/your_video_id/0.jpg)](https://youtu.be/your_video_id)

---

## 🛠️ How to Run

### 1. Clone this repo
```bash
git clone https://github.com/stutiyadav/sign-o-calc.git
cd sign-o-calc
