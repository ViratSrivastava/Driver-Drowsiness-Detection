import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("weights/cnn_driver_drowsiness_detection-m4.h5")

# Function to preprocess frames for prediction
def preprocess_frame(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    resized_frame = cv2.resize(gray_frame, (64, 64))  # Resize to model input size
    normalized_frame = resized_frame / 255.0  # Normalize pixel values
    preprocessed_frame = np.expand_dims(normalized_frame, axis=-1)  # Add channel dimension
    preprocessed_frame = np.expand_dims(preprocessed_frame, axis=0)  # Add batch dimension
    return preprocessed_frame

# Use the external webcam (index 1)
camera_index = 0
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print(f"Error: Camera with index {camera_index} is not available.")
    exit()

print(f"Camera with index {camera_index} is working.")
print("Press 'q' to exit the video feed.")

while True:
    ret, frame = cap.read()  # Capture a single frame
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Preprocess the captured frame
    preprocessed_frame = preprocess_frame(frame)

    # Make predictions
    predictions = model.predict(preprocessed_frame)

    # Process predictions
    if predictions.shape == (1, 1):  # Binary classification
        closed_eyes_confidence = predictions[0][0] * 100
        open_eyes_confidence = (1 - predictions[0][0]) * 100

        # Overlay predictions on the video feed
        cv2.putText(frame, f'Closed Eyes: {closed_eyes_confidence:.2f}%', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f'Open Eyes: {open_eyes_confidence:.2f}%', (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    else:
        cv2.putText(frame, "Unexpected prediction shape", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Driver Drowsiness Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting video feed...")
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
print("Video feed closed and resources released.")
