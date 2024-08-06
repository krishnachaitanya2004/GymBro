import tensorflow as tf
import tensorflow_hub as hub
import model
import cv2

video = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = video.read()
    cv2.imwrite("pose"+str(count)+".jpg", frame)
    model.model("pose"+str(count)+".jpg")
    count += 1
    if count == 5:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
video.destroyAllWindows()
