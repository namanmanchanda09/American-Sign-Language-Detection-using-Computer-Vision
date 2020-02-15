import os
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time

# Loading the model
model = load_model('hack36_2.h5')


video = cv2.VideoCapture(0)

# msg = ''

while True:
        _, frame = video.read()
        cv2.rectangle(frame,pt1=(100,100),pt2=(300,300),color=(0,255,0),thickness=6)
        
#         frame_arr = np.asarray(frame)
        
        
        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')
        #print(type(im))
        
        #Resizing into 64x64
#         im = im.resize((64,64))
        img_array = np.asarray(frame)
            
        clone = img_array[100:300, 100:300].copy()
#         plt.imshow(clone)
#         plt.show()
        clone_resized = cv2.resize(clone, (64,64))
#         print(clone_resized.shape)
#         plt.imshow(clone_resized)
       
        img_array=clone_resized/255
        
        
#         img = Image.fromarray(clone_resized, 'RGB')
#         img_gray = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)
#         img_array=img_gray/255
#         img_array_gray = np.array(img_array)
                
#         print(img_array.shape)
        #Our keras model used a 4D tensor, (images x height x width x channel)
        img_final = np.expand_dims(img_array, axis=0)
        
#         img_final = np.reshape(img_semi_final, (-1, 64, 64, 1))
      
        prediction = model.predict(img_final)

#         print(np.argmax(prediction))

        label = np.argmax(prediction)

        msg = ''
        if label == 0:
            msg += 'A'
        elif label == 1:
            msg += 'B'
        elif label == 2:
            msg += 'C'
        elif label == 3:
            msg += 'D'
        elif label == 4:
            msg += 'E'
        elif label == 5:
            msg += 'F'
        elif label == 6:
            msg += 'G'
        elif label == 7:
            msg += 'H'
        elif label == 8:
            msg += 'I'
        elif label == 9:
            msg += 'J'
        elif label == 10:
            msg += 'K'
        elif label == 11:
            msg += 'L'
        elif label == 12:
            msg += 'M'
        elif label == 13:
            msg += 'N'
        elif label == 14:
            msg += 'O'
        elif label == 15:
            msg += 'P'
        elif label == 16:
            msg += 'Q'
        elif label == 17:
            msg += 'R'
        elif label == 18:
            msg += 'S'
        elif label == 19:
            msg += 'T'
        elif label == 20:
            msg += 'U'
        elif label == 21:
            msg += 'V'
        elif label == 22:
            msg += 'W'
        elif label == 23:
            msg += 'X'
        elif label == 24:
            msg += 'Y'
        elif label == 25:
            msg += 'Z'
#         elif label == 26:
#             msg += '-del-'
        elif label == 27:
            msg += '<nothing>'
        elif label == 28:
            msg += ' '
        
        print(msg)
        time.sleep(0.2)
        
        
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()

print(msg)