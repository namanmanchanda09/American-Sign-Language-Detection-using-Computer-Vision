import os
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import collections
import win32com.client as winc1



v = winc1.Dispatch("SAPI.SpVoice")

# Loading the model
model = load_model('hack36_2.h5')


def max_char(text):
    return collections.Counter(text).most_common(1)[0][0]

# Don't touch this cell

video = cv2.VideoCapture(0)
text=''
flag=[]
frame_count = 0
while True:
        _, frame = video.read()
        cv2.rectangle(frame,pt1=(100,100),pt2=(300,300),color=(0,255,0),thickness=6)
        
        frame_count += 1
        
        if frame_count%150 == 0:
            
            im = Image.fromarray(frame, 'RGB')

            img_array = np.asarray(frame)

            clone = img_array[100:300, 100:300].copy()

            clone_resized = cv2.resize(clone, (64,64))

            img_array=clone_resized/255

            img_final = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_final)

            label = np.argmax(prediction)
            
            if label == 0:
                ch = 'A'
            elif label == 1:
                ch = 'B'
            elif label == 2:
                ch = 'C'
            elif label == 3:
                ch = 'D'
            elif label == 4:
                ch = 'E'
            elif label == 5:
                ch =  'F'
            elif label == 6:
                ch = 'G'
            elif label == 7:
                ch = 'H'
            elif label == 8:
                ch = 'I'
            elif label == 9:
                ch = 'J'
            elif label == 10:
                ch = 'K'
            elif label == 11:
                ch = 'L'
            elif label == 12:
                ch = 'M'
            elif label == 13:
                ch = 'N'
            elif label == 14:
                ch = 'O'
            elif label == 15:
                ch = 'P'
            elif label == 16:
                ch = 'Q'
            elif label == 17:
                ch = 'R'
            elif label == 18:
                ch = 'S'
            elif label == 19:
                ch = 'T'
            elif label == 20:
                ch = 'U'
            elif label == 21:
                ch = 'V'
            elif label == 22:
                ch = 'W'
            elif label == 23:
                ch = 'X'
            elif label == 24:
                ch = 'Y'
            elif label == 25:
                ch = 'Z'
                                
            elif label == 26:
#                 m = max_char(text)
#                 text=m
#                 flag=flag+text
#                 text=''
                                  # Delete
                ch=''
#                 text = ''
                
                                
            elif label == 27:#Nothing
#                 m = max_char(text)
#                 flag = flag + m
                ch=''
                
                
            elif label == 28:     # Space
                
                ch = ' '
                print('space')
        
            flag.append(ch)
            print(ch)
            
        

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break

text=''
for i in flag:
    text+=i

# for i in range(len(flag)):
#     if (i==0 and flag[i] == '*'):
#         continue
#     elif(flag[i]=='*'):
#         text=text+flag[i-1]
        

video.release()
cv2.destroyAllWindows()


print(text)
v.Speak(text)