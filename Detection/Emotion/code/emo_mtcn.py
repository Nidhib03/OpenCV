from fer import FER
from fileinput import filename
# from string import hexdigits
from turtle import color, width
import mtcnn
import matplotlib.pyplot as plt
# from numpy import rint

filename=("/home/rao/anaconda3/envs/Emotion/train/Disguist/images (7).jpg")
test_image_one = plt.imread(filename)              # Disguist img7, angry down17, fear img11, neutral down12, sad img5, surprise img4
emo_detector = FER(mtcnn=True)
captured_emotions = emo_detector.detect_emotions(test_image_one)

plt.imshow(test_image_one)

def draw_facebox(filename, result_list):
        # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    print(dominant_emotion,':', emotion_score)
    
    ax= plt.gca()
    for result in result_list:
        x,y, w, h = result['box']
        rect = plt.Rectangle((x,y), w, h, fill=False, color='brown')
        plt.fill_betweenx(dominant_emotion, emotion_score)
        # plt.axis("on")
        ax.add_patch(rect)
    plt.show()
detector = mtcnn.MTCNN()
faces = detector.detect_faces(test_image_one)
draw_facebox(filename,faces)
print(captured_emotions)