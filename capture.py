import cv2

# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Read the video stream
ret, frame = cap.read()

m="h"
# Specify the file path to save the captured image
file_path = "D:/Vision Of Us/New folder (2)/"+m+'.jpg'

# Save the captured image to disk
cv2.imwrite(file_path, frame)

# Release the camera
cap.release()

# Print a message to indicate that the image has been saved successfully
print("Image saved to", file_path)
