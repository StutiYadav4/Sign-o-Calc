# Sign-o-Calc
> A gesture-controlled calculator built using OpenCV, MediaPipe, and Python

---

## What is Sign-o-Calc?

**Sign-o-Calc** is a real-time, gesture-based calculator that allows you to perform arithmetic operations using only hand gestures. Using a webcam and hand tracking via MediaPipe, it recognizes different finger combinations to represent numbers and mathematical operators.

Whether you're working on math or just exploring gesture recognition, Sign-o-Calc provides a hands-free and interactive way to evaluate expressions.

---

## Features

- Real-time gesture recognition using MediaPipe and OpenCV
- Full digit support (0–9) through intuitive finger combinations
- Supports arithmetic operations: `+`, `-`, `*`, `/`, `=`, `C` (Clear)
- Includes advanced operations: `^` (power), `√` (square root), `(`, `)`, and `.`
- Automatically evaluates valid expressions and displays results
- Live on-screen expression updates
- Error-handling for invalid expressions

---

## Live Demo

▶️ [Live Demo](https://drive.google.com/file/d/1VEp-ocZ3whij9FCrFjuvzPHI47F0kVPA/view?usp=drive_link)

---

## Gesture Mappings

### Right Hand: Numbers and Basic Operators

| Gesture                       | Input |
|------------------------------|-------|
| Middle Finger                | `=`   |
| Pinky only                   | `+`   |
| Thumb + Pinky                | `/`   |
| Index + Pinky                | `*`   |
| Thumb + Index + Pinky        | `-`   |
| Ring finger only             | `C` (Clear) |
| Index                        | `1`   |
| Index + Middle               | `2`   |
| Index + Middle + Ring        | `3`   |
| Index + Middle + Ring + Pinky| `4`   |
| All fingers                  | `5`   |
| Thumb                        | `6`   |
| Thumb + Index                | `7`   |
| Thumb + Index + Middle       | `8`   |
| Thumb + Index + Middle + Ring| `9`   |
| Thumb + Middle + Ring + Pinky| `0`   |

### Left Hand: Special Symbols

| Fingers Up | Symbol |
|------------|--------|
| 1 (Index)  | `^`    |
| 2 fingers  | `√`    |
| 3 fingers  | `(`    |
| 4 fingers  | `)`    |
|All 5 fingers| `.`    |

---

## Installation

### Clone the repository
```bash
git clone https://github.com/stutiyadav/sign-o-calc.git
cd sign-o-calc
