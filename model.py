import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import get_angles   

def diff_angles(angles1,angles2):
    diff = {}
    for key in angles1:
        diff[key] = abs(angles1[key] - angles2[key])
    return diff

def sum(diff):
    total_diff = 0
    for key in diff:
        total_diff += diff[key]
    return total_diff

def model(image_path):
   image = tf.io.read_file(image_path)
   image = tf.image.decode_jpeg(image)
   image = tf.expand_dims(image, axis=0)
   image = tf.cast(tf.image.resize_with_pad(image, 256, 256), dtype=tf.int32)

   model = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")
   movenet = model.signatures['serving_default']

   outputs = movenet(image)

   keypoints = outputs['output_0'].numpy().reshape(-1,3)

   angles = get_angles.get_angles(keypoints)
   return keypoints,angles
   
   

