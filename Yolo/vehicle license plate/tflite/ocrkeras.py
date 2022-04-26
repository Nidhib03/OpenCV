import matplotlib.pyplot as plt
import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()

images = [
keras_ocr.tools.read(url) for url in [
    'https://storage.googleapis.com/gcptutorials.com/examples/keras-ocr-img-1.jpg',        
    'https://storage.googleapis.com/gcptutorials.com/examples/keras-ocr-img-2.png'
]
]
# print(images[0])
# print(images[1])

prediction_groups = pipeline.recognize(images)

predicted_image_1 = prediction_groups[0]
for text, box in predicted_image_1:
    print(text)

predicted_image_2 = prediction_groups[1]
for text, box in predicted_image_2:
    print(text)



'''on tflite model'''

import string
from tkinter.messagebox import NO
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import keras_ocr

model_path = 'model.tflite'
classes = ['license_plate']

COLORS = np.random.randint(0, 255, size=(len(classes), 3), dtype=np.uint8)

all_dir = os.listdir('images')

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("flowing-radio-347411-f6b13db7738b.json", scopes)
file = gspread.authorize(credentials) 
sheet = file.open("Number plate Recognition").get_worksheet(10)
header = ["Date", "Number plate"]
sheet.insert_row(header)

pipeline = keras_ocr.pipeline.Pipeline()

for image in all_dir:
    path = 'images/'+image
    im = Image.open(path)
    im.thumbnail((512, 512), Image.ANTIALIAS)
    string = image.split(".")[0]
    tlist=[]
    l = len(sheet.col_values(1)) 
    l += 1
    sheet.update('A'+str(l),string)
    
    def preprocess_image(image_path, input_size):
      img = tf.io.read_file(image_path)
      img = tf.io.decode_image(img, channels=3)
      img = tf.image.convert_image_dtype(img, tf.uint8)
      original_image = img
      resized_img = tf.image.resize(img, input_size)
      resized_img = resized_img[tf.newaxis, :]
      resized_img = tf.cast(resized_img, dtype=tf.uint8)
      return resized_img, original_image

    def detect_objects(interpreter, image, threshold):
      signature_fn = interpreter.get_signature_runner()
      output = signature_fn(images=image)
      count = int(np.squeeze(output['output_0']))
      scores = np.squeeze(output['output_1'])
      classes = np.squeeze(output['output_2'])
      boxes = np.squeeze(output['output_3'])
      results = []
      for i in range(count):
        if scores[i] >= threshold:
          result = {
            'bounding_box': boxes[i],
            'class_id': classes[i],
            'score': scores[i]
          }
          results.append(result)
      return results

    def run_odt_and_draw_results(image_path, interpreter, threshold=0.5):
      _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']
      preprocessed_image, original_image = preprocess_image(
          image_path,
          (input_height, input_width)
        )
      # results gives detected object from image- here num plate from vehicle's images
      results = detect_objects(interpreter, preprocessed_image, threshold=threshold)
      # print("result", results)
      original_image_np = original_image.numpy().astype(np.uint8)
      for obj in results:
        
        temp_NP_List = []

        ymin, xmin, ymax, xmax = obj['bounding_box']
        xmin = int(xmin * original_image_np.shape[1])
        xmax = int(xmax * original_image_np.shape[1])
        ymin = int(ymin * original_image_np.shape[0])
        ymax = int(ymax * original_image_np.shape[0])
        class_id = int(obj['class_id'])
        color = [int(c) for c in COLORS[class_id]]
        im = cv2.rectangle(original_image_np, (xmin, ymin), (xmax, ymax), color, 2)
        crop = im[ymin:ymax, xmin:xmax]
        
        try:
          images = [keras_ocr.tools.read(img) for img in [crop]]
          prediction_groups = pipeline.recognize(images)

          for i in prediction_groups:
            for text, box in i:
                print("text :::::::::", text)
                temp_NP_List.append(text)
            temp_NP_List.remove('ind')
        except:
          pass
        print("temp_NP_List :::::::::::::::::",temp_NP_List)
        num = (''.join(temp_NP_List))
        print("Number plate:::",num)
        tlist.append(num)
        print(tlist)
        print("one plate detected")

        sheet.update('B'+str(l),[tlist])

      original_uint8 = original_image_np.astype(np.uint8)
      return original_uint8

    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    DETECTION_THRESHOLD = 0.3
    detection_result_image = run_odt_and_draw_results(
        path,
        interpreter,
        threshold=DETECTION_THRESHOLD
    )
i  = Image.fromarray(detection_result_image)
i.show()
