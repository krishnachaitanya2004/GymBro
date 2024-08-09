import cv2
import model

video1 = cv2.VideoCapture('pushup.gif')
video2 = cv2.VideoCapture('wrong_pushup.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out1 = cv2.VideoWriter('output_pushup.mp4', fourcc, 30.0, (int(video1.get(3)), int(video1.get(4))))
out2 = cv2.VideoWriter('output_wrong_pushup.mp4', fourcc, 30.0, (int(video2.get(3)), int(video2.get(4))))


# Trainer data will be stored and will be compared with user's key frames.
# Key frames of trainer will be searched in users exercise.
# If some percentage of frames match, we can count it to be 1
prvs_angles = None
diff_sum = 99999
threshold = 45
while True:
    ret1, frame1 = video1.read()
    if not ret1:
        break
    keypoints1, angles1 = model.get_data(frame1)
    if prvs_angles:
        diff = model.diff_angles(prvs_angles, angles1)
        diff_sum = model.sum(diff)
    if(diff_sum > threshold):
        ## Store in csv file
        print("Hello")




while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    if not ret1 or not ret2:
        break
    
    keypoints1, angles1 = model.get_data(frame1)
    keypoints2, angles2 = model.get_data(frame2)


    diff = model.diff_angles(angles1, angles2)
    diff_sum = model.sum(diff)

    print(diff_sum)

    #show keypoints on frame1 and frame2
    height, width, _ = frame1.shape
    for keypoint in keypoints1:
        y, x, confidence = keypoint
        if confidence > 0.3:
            x = int(x * width)
            y = int(y * height)
            cv2.circle(frame1, (x, y), 5, (0, 0, 255), -1)

    height, width, _ = frame2.shape
    for keypoint in keypoints2:
        y, x, confidence = keypoint
        if confidence > 0.3:
            x = int(x * width)
            y = int(y * height)
            cv2.circle(frame2, (x, y), 5, (0, 0, 255), -1)    

    out1.write(frame1)
    out2.write(frame2)
    
    cv2.imshow("Frame1", frame1)
    cv2.imshow("Frame2", frame2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video1.release()
video2.release()
out1.release()
out2.release()