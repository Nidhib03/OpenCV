from fer import FER
import matplotlib.pyplot as plt

test_image_one = plt.imread("/home/rao/anaconda3/envs/Emotion/train/Neutral/download (12).jpg")              # Disguist img7, angry down17, fear img11, neutral down12, sad img5, surprise img4
emo_detector = FER(mtcnn=True)
captured_emotions = emo_detector.detect_emotions(test_image_one)
print(captured_emotions)
plt.imshow(test_image_one)
# Use the top Emotion() function to call for the dominant emotion in the image
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(dominant_emotion, emotion_score)
