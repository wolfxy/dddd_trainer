import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import os

imgdir = "D:\\Users\\wuquancheng\\Desktop\\vocde\\test"
for filename in os.listdir(imgdir):
    f = os.path.join(imgdir, filename)
    img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f, img)
