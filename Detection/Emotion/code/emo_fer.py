import cv2
from fer import FER
detector = FER(mtcnn=True) 
image = cv2.imread("/home/rao/anaconda3/envs/Emotion/train/Surprise/images (25).jpg")
result = detector.detect_emotions(image)
# print(result)
bounding_box = result[0]["box"]
emotions = result[0]["emotions"]

cv2.rectangle(image,(bounding_box[0], bounding_box[1]),
(bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),(165, 248, 255), 1,)

for idx, (emotion, score) in enumerate(emotions.items()):
    color = (211, 211, 211) if score < 0.01 else (255, 0, 0)
    emotion_score = "{}: {}".format(
          emotion, "{:.2f}".format(score) if score > 0.01 else ""
        )
    cv2.putText(image,emotion_score,
            (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + idx * 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,1,cv2.LINE_AA,)
    print(emotion, score)

cv2.imshow('img', image)
cv2.waitKey()

