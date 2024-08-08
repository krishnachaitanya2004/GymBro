import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np

# Load the MoveNet model from TF Hub.
model = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
movenet = model.signatures['serving_default']

# Function to run the model on an image and get keypoints.
def run_inference(image):
    # Convert the image to a tensor and resize to 256x256.
    image_tensor = tf.image.resize_with_pad(image, 256, 256)
    image_tensor = tf.cast(image_tensor, dtype=tf.int32)
    image_tensor = tf.expand_dims(image_tensor, axis=0)
    
    # Run the model.
    outputs = movenet(image_tensor)
    keypoints = outputs['output_0'].numpy()[0, 0, :, :]
    
    return keypoints

# Open the video file.
video = cv2.VideoCapture('pushup.gif')

# Get video properties.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
fps = int(video.get(cv2.CAP_PROP_FPS))

# Initialize VideoWriter before the loop.
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    # Convert frame to RGB.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = tf.convert_to_tensor(image, dtype=tf.uint8)
    
    # Run inference.
    keypoints = run_inference(image)
    
    # Draw keypoints on the original frame.
    height, width, _ = frame.shape
    for keypoint in keypoints:
        y, x, confidence = keypoint
        if confidence > 0.3:
            # Scale x and y back to the original image size.
            x = int(x * width)
            y = int(y * height)
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
    
    # Write the frame with keypoints to the output video.
    out.write(frame)
    
    # Show the frame.
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything.
video.release()
out.release()
cv2.destroyAllWindows()

#save the video with keypoints


