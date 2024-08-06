import cv2
import os
import model

def process_frame(frame, count, angles):
    frame_resized = cv2.resize(frame, (256, 256))
    filename = f"pose{count}.jpg"
    cv2.imwrite(filename, frame_resized)
    angles1 = model.model(filename)  # Pass the filename to the model
    angle_diff = sum(abs(angles[key] - angles1[key]) for key in angles)
    if angle_diff < 45:
        os.remove(filename)
    else:
        angles = angles1
    return angles

def main():
    video = cv2.VideoCapture("video.mp4")
    count = 0
    ret, frame = video.read()
    
    if not ret:
        print("Failed to read video")
        return
    
    initial_filename = "initial_pose.jpg"
    cv2.imwrite(initial_filename, cv2.resize(frame, (256, 256)))
    angles = model.model(initial_filename)
    count += 1
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        if count % 10 == 0:  # Skip 4 out of 5 frames
            angles = process_frame(frame, count, angles)
        
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
