# Landmark tips
finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

def get_fingers_up(hand_landmarks, handedness):
    fingers = []

    # Thumb
    if handedness == "Right":
        fingers.append(1 if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)

    # Other fingers
    for tip in finger_tips[1:]:
        fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)

    return fingers  # [thumb, index, middle, ring, pinky]

def gesture_to_input(fingers_list, handedness_list):
    result = None
    if not fingers_list:
        return result

    for fingers, hand in zip(fingers_list, handedness_list):
        gesture = tuple(fingers)
        fingers_up = sum(fingers)

        if hand == "Right":
            gestures = {
                (0, 0, 1, 0, 0): '=',      # Middle only
                (0, 0, 0, 1, 0): 'C',      # Ring only = Clear
                (0, 1, 0, 0, 0): '1',
                (0, 1, 1, 0, 0): '2',
                (0, 1, 1, 1, 0): '3',
                (0, 1, 1, 1, 1): '4',
                (1, 1, 1, 1, 1): '5',
                (1, 0, 0, 0, 0): '6',
                (1, 1, 0, 0, 0): '7',
                (1, 1, 1, 0, 0): '8',
                (1, 1, 1, 1, 0): '9',
                (1, 0, 1, 1, 1): '0',
                (0, 0, 0, 0, 1): '+',
                (1, 0, 0, 0, 1): '/',
                (0, 1, 0, 0, 1): '*',
                (1, 1, 0, 0, 1): '-',
            }
            result = gestures.get(gesture, None)

        elif hand == "Left":
            # 1 to 5 fingers up for symbols
            left_specials = {
                1: '^',
                2: '√',
                3: '(',
                4: ')',
                5: '.'
            }
            result = left_specials.get(fingers_up, None)

        if result:
            break

    return result