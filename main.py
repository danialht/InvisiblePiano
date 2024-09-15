import cv2 as cv
import mediapipe as mp
import numpy as np
import math
from Piano import Piano


piano_window = Piano()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

ANGLE_THRESHOLD = 20

capture = cv.VideoCapture(0)

# Landmark point numbers that we are interested in
points = [
    0,              # bottommost point of hand
    5, 7,    # Index finger
    9, 11,   # Middle finger
    13, 15,  # Ring finger
    17, 19,  # Pinky finger
    ]

is_pressed = [False for _ in range(8)]

while True:
    """
    TODO: Write the docstring
    """
    piano_window.update()
    can_read, frame = capture.read()
    if not can_read:
        break

    frame = cv.flip(frame, 1)

    # Convert BGR image to RGB for MediaPipe
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Process the image with MediaPipe hands
    results = hands.process(image)

    # Draw hand landmarks and connections
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            

    if results.multi_hand_landmarks:
        angles = []
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the index finger tip
            index_finger_tip = hand_landmarks.landmark[8]


            # finding an angle for each finger
            
            bottom_pos = np.array([hand_landmarks.landmark[points[0]].x * image.shape[1], hand_landmarks.landmark[points[0]].y * image.shape[0]])
            
            for i in range(1, len(points), 2):
                pos1 = np.array([hand_landmarks.landmark[points[i]].x * image.shape[1], hand_landmarks.landmark[points[i]].y * image.shape[0]])
                pos2 = np.array([hand_landmarks.landmark[points[i + 1]].x * image.shape[1], hand_landmarks.landmark[points[i + 1]].y * image.shape[0]])
                
                relative_vec1 = pos1 - bottom_pos
                relative_vec2 = pos2 - pos1
                
                angle = 180 / math.pi * math.acos(np.dot(relative_vec1, relative_vec2) / (np.linalg.norm(relative_vec1) * np.linalg.norm(relative_vec2)))
                
                angles.append(angle)
                
        for i in range(len(angles)):
            if angles[i] > ANGLE_THRESHOLD and not is_pressed[i]:
                is_pressed[i] = True
                piano_window.press_key(i)
                
            elif angles[i] < ANGLE_THRESHOLD and is_pressed[i]:
                is_pressed[i] = False
                piano_window.unpress_key(i)
        
        print(is_pressed)
        
        #if(len(angles) != 8):
        #    cv.putText(frame, "Both of your hands must be visible!", (0, 30), cv.FONT_HERSHEY_TRIPLEX, 0.9, (255, 0, 255), 2)
         

    cv.imshow('Invisible Piano', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()