import mtcnn
import cv2
detector = mtcnn.MTCNN()
#Load a videopip TensorFlow
cap = cv2.VideoCapture(-1)
 
while (True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))
    boxes = detector.detect_faces(frame)
    if boxes:
        box = boxes[0]['box']
        conf = boxes[0]['confidence']
        x, y, w, h = box[0], box[1], box[2], box[3]
 
        if conf > 0.5:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (156, 255, 5), 3)
 
    cv2.imshow("Frame", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()