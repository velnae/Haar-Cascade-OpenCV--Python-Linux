import urllib.request
import cv2
import numpy as np
import os

def generate_images_neg():
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for file_type in ['fondos']:
        for img in os.listdir(file_type):
            try:
                print(img)
                img = cv2.imread("fondos/"+str(img), cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (100, 100))
                cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
                pic_num += 1
                
            except Exception as e:
                print(str(e))  

generate_images_neg()