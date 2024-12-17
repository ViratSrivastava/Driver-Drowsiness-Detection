import os
import cv2 # type: ignore
import numpy as np
import tensorflow as tf

# Check if the model file exists
model_path = "weights/cnn_driver_drowsiness_detection-m1.h5"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"No file or directory found at {model_path}")
# Load the trained model
model = tf.keras.models.load_model(model_path)
# Start video capture from the camera (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Preprocess the frame for prediction
    img = cv2.resize(frame, (80, 80))  # Resize to match model input size
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make predictions
    predictions = model.predict(img_array)
    
    # Get confidence scores for both classes
    closed_eyes_confidence = predictions[0][0] * 100  # Assuming index 0 is for closed eyes
    open_eyes_confidence = predictions[0][1] * 100     # Assuming index 1 is for open eyes

    # Display confidence scores on the frame
    cv2.putText(frame, f'Closed Eyes Confidence: {closed_eyes_confidence:.2f}%', 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f'Open Eyes Confidence: {open_eyes_confidence:.2f}%', 
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Check if confidence score exceeds threshold (e.g., closed eyes)
    if closed_eyes_confidence > 65:
        cv2.putText(frame, "ALERT: Closed Eyes!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show video feed with predictions overlayed
    cv2.imshow('Live Video Feed', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
