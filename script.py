import os
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Loading the model
model = load_model('hack36_2.h5')


