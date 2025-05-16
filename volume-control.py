import cv2
import mediapipe as mp
import pyautogui

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils


while True:

    _ , image = webcam.read()
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:  
            drawing_utils.draw_landmarks(image,hand)  

    cv2.imshow("Hand Volume Control Using Python", image)
    
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()