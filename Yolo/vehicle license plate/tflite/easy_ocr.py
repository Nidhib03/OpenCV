import string
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
# import easyocr
import csv
import pandas as pd
import os
from easyocr import Reader
import argparse

model_path = 'model.tflite'
classes = ['license_plate']
COLORS = np.random.randint(0, 255, size=(len(classes), 3), dtype=np.uint8)

'''load image from folder'''
all_dir = os.listdir('images')

for image in all_dir:
    # print(image)
    path = 'images/'+image
    im = Image.open(path)
    im.thumbnail((512, 512), Image.ANTIALIAS)
    string = image.split(".")[0]
    # print("string ::: ", string)

    def preprocess_image(image_path, input_size):
      """Preprocess the input image to feed to the TFLite model"""
      img = tf.io.read_file(image_path)
      img = tf.io.decode_image(img, channels=3)
      img = tf.image.convert_image_dtype(img, tf.uint8)
      original_image = img
      resized_img = tf.image.resize(img, input_size)
      resized_img = resized_img[tf.newaxis, :]
      resized_img = tf.cast(resized_img, dtype=tf.uint8)
      return resized_img, original_image

    def detect_objects(interpreter, image, threshold):
      """Returns a list of detection results, each a dictionary of object info."""
      signature_fn = interpreter.get_signature_runner()

      # Feed the input image to the model
      output = signature_fn(images=image)

      # Get all outputs from the model
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
      """Run object detection on the input image and draw the detection results"""
      
      # Load the input shape required by the model
      _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

      # Load the input image and preprocess it
      preprocessed_image, original_image = preprocess_image(
          image_path,
          (input_height, input_width)
        )
      # Run object detection on the input image
      results = detect_objects(interpreter, preprocessed_image, threshold=threshold)
      
      # Plot the detection results on the input image
      original_image_np = original_image.numpy().astype(np.uint8)
      for obj in results:
        # Convert the object bounding box from relative coordinates to absolute
        # coordinates based on the original image resolution
        ymin, xmin, ymax, xmax = obj['bounding_box']
        xmin = int(xmin * original_image_np.shape[1])
        xmax = int(xmax * original_image_np.shape[1])
        ymin = int(ymin * original_image_np.shape[0])
        ymax = int(ymax * original_image_np.shape[0])

        # Find the class index of the current object
        class_id = int(obj['class_id'])
        
        # Draw the bounding box and label on the image
        color = [int(c) for c in COLORS[class_id]]
        im = cv2.rectangle(original_image_np, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.imshow('box', im)
        cv2.waitKey(0)
        
        '''crop image from bounding box'''
        
        crop = im[ymin:ymax, xmin:xmax]
        # cv2.imwrite("Cropped.jpg", crop)
        # cv2.imshow("cropped", crop)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        '''easyOCR'''

        def cleanup_text(text):
              # strip out non-ASCII text so we can draw the text on the image using OpenCV
          return "".join([c if ord(c) <= 90 else "" for c in text]).strip()

        ap = argparse.ArgumentParser()
        # ap.add_argument("-i", "--image", required=True,
          # help="path to input image to be OCR'd")
        ap.add_argument("-l", "--langs", type=str, default="en",
          help="comma separated list of languages to OCR")
        ap.add_argument("-g", "--gpu", type=int, default=-1,
          help="whether or not GPU should be used")
        args = vars(ap.parse_args())

        # break the input languages into a comma separated list
        langs = args["langs"].split(",")
        print("img path", string)
        print("[INFO] OCR'ing with the following languages: {}".format(langs))
    
        reader = Reader(langs, gpu=args["gpu"] > 0)
        results = reader.readtext(crop)
        for (bbox, text, prob) in results:
          print("[INFO] {:.4f}: {}".format(prob, text))
          text = cleanup_text(text)
          
          '''OR'''      
        # reader = easyocr.Reader(['en'])
        # result = reader.readtext(crop)
        # # print("result",result)
        # txt = ''
        # for res in result:
        #       txt += res[1]
        # print("LICENSE PLATE NUMBER :::::::::",txt)
        
        # df = pd.DataFrame(columns=['Date', 'Number plate'])
        # df = df.append({'Date':string, 'Number plate':txt}, ignore_index = True)
        '''OR with create empty df'''
        # df = pd.DataFrame()
        # print(df)
        # df['Date'] = [string]
        # df['Number plate'] = [txt]
        # print(df.to_string(index=False))
        # df.to_csv('dataframe.csv', index=False)
        
        with open("data.csv", "a") as csvfile:                    # mode='w'
          writer = csv.writer(csvfile)
          # writer.writerow(["Date", "Number Plate"])
          writer.writerow([string, text])
        
        # Make adjustments to make the label visible for all objects
        y = ymin - 15 if ymin - 15 > 15 else ymin + 15
        label = "{}: {:.0f}%".format(classes[class_id], obj['score'] * 100)
        cv2.putText(original_image_np, label, (xmin, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

      # Return the final image
      original_uint8 = original_image_np.astype(np.uint8)
      return original_uint8
    
    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    
    DETECTION_THRESHOLD = 0.3
    # Run inference and draw detection result on the local copy of the original file
    detection_result_image = run_odt_and_draw_results(
        path,
        interpreter,
        threshold=DETECTION_THRESHOLD
    )

# Show the detection result
i  = Image.fromarray(detection_result_image)
i.show()

