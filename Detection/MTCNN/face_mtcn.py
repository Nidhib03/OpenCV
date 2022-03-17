from fileinput import filename
from string import hexdigits
from turtle import color, width
import mtcnn
# print(mtcnn.__version__)

import matplotlib.pyplot as plt
from numpy import rint

filename= "/home/rao/anaconda3/envs/Detect/2.jpg"
pixels= plt.imread(filename)
# print("Shape of image/array:",pixels.shape)
# imgplot= plt.imshow(pixels)
# plt.show()
def draw_facebox(filename, result_list):
    data = plt.imread(filename)
    plt.imshow(data)
    ax= plt.gca()
    for result in result_list:
        x,y, width, height = result['box']
        rect = plt.Rectangle((x,y), width, height, fill=False, color='yellow')
        ax.add_patch(rect)
    plt.show()
detector = mtcnn.MTCNN()
faces = detector.detect_faces(pixels)
draw_facebox(filename, faces)
