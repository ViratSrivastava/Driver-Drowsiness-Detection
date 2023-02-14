import cv2
import dlib
import pygame
import time
import imutils
from scipy.spatial import distance as dist

# Define constants for eye aspect ratio (EAR) threshold, number of consecutive frames
# the eye must be below the threshold for, and the alarm sound file path
EAR_THRESHOLD = 0.25
NUM_CONSEC_FRAMES = 30
ALARM_SOUND_PATH = "alarm.wav"

# Initialize the dlib face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the Pygame sound mixer
pygame.mixer.init()

# Load the alarm sound
alarm_sound = pygame.mixer.Sound(ALARM_SOUND_PATH)

# Initialize the video stream and wait for the camera to warm up
cap = cv2.VideoCapture(0)
time.sleep(2.0)

# Initialize variables to track the number of consecutive frames the eye has been closed
closed_frames = 0

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Resize the frame and convert it to grayscale
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray, 0)

    # Loop over each face in the frame
    for face in faces:
        # Get the facial landmarks for the face
        landmarks = predictor(gray, face)

        # Extract the left and right eye coordinates from the landmarks
        left_eye_coords = [(landmarks.part(36).x, landmarks.part(36).y),
                           (landmarks.part(37).x, landmarks.part(37).y),
                           (landmarks.part(38).x, landmarks.part(38).y),
                           (landmarks.part(39).x, landmarks.part(39).y),
                           (landmarks.part(40).x, landmarks.part(40).y),
                           (landmarks.part(41).x, landmarks.part(41).y)]
        right_eye_coords = [(landmarks.part(42).x, landmarks.part(42).y),
                            (landmarks.part(43).x, landmarks.part(43).y),
                            (landmarks.part(44).x, landmarks.part(44).y),
                            (landmarks.part(45).x, landmarks.part(45).y),
                            (landmarks.part(46).x, landmarks.part(46).y),
                            (landmarks.part(47).x, landmarks.part(47).y)]

        # Calculate the Eye Aspect Ratio (EAR) for each eye
        left_ear = dist.euclidean(left_eye_coords[1], left_eye_coords[5]) / \
                   dist.euclidean(left_eye_coords[2], left_eye_coords[4])
        right_ear = dist.euclidean(right_eye_coords[1], right_eye_coords[5]) / \
                    dist.euclidean(right_eye_coords[2], right_eye_coords[4])

        # Average the EAR for both eyes
        ear = (left_ear + right_ear) / 2.0

        # Draw the eye regions on the frame
        cv2.polylines(frame, [left_eye_coords], True, (0, 0, 255), 1)
        cv2.polylines(frame, [right_eye_coords], True, (0, 0, 255), 1)

       
