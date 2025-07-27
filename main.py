import mediapipe as mp
import time
import cv2
import re
from math import sqrt


# Start video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

expression = ""
last_input = ""
last_gesture_time = 0
gesture_delay = 2.0

print("\n--- Gesture Calculator ---")
print("• Right-hand → Digits and basic operators")
print("• Left-hand 1-5 fingers → ^, √, (, ), .")
print("• Middle finger only → '='")
print("• Ring finger only → 'C' (Clear)")
print("• Press 'q' to quit\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()
    symbol = None

    if results.multi_hand_landmarks and results.multi_handedness:
        fingers_list = []
        handedness_list = []

        for i, (hand_landmarks, handedness) in enumerate(zip(results.multi_hand_landmarks, results.multi_handedness)):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand_label = handedness.classification[0].label
            handedness_list.append(hand_label)
            fingers = get_fingers_up(hand_landmarks, hand_label)
            fingers_list.append(fingers)

        if current_time - last_gesture_time > gesture_delay:
            symbol = gesture_to_input(fingers_list, handedness_list)

            if symbol and symbol != last_input:
                if symbol == '=':
                    if expression:
                        expression = safe_eval(expression)
                elif symbol == 'C':
                    expression = ""
                else:
                    expression += symbol

                last_input = symbol
                last_gesture_time = current_time
                print(f"Gesture: {symbol} | Expression: {expression}")

    else:
        if current_time - last_gesture_time > gesture_delay:
            last_input = ""

    # UI Elements
    cv2.rectangle(frame, (0, 0), (w, 100), (30, 30, 30), -1)

    # Show current symbol
    if symbol:
        cv2.putText(frame, f"Gesture: {symbol}", (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 255, 255), 3)

    # Show current expression
    cv2.putText(frame, f"Expr: {expression if expression else '0'}",
                (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 200, 200), 2)

    # Timer / Ready
    time_left = max(0, gesture_delay - (current_time - last_gesture_time))
    if time_left > 0:
        cv2.putText(frame, f"Wait: {time_left:.1f}s", (w - 170, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    else:
        cv2.putText(frame, "Ready for gesture", (w - 220, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Gesture Calculator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Calculator closed.")