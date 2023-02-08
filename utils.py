import cv2
import random
import numpy as np

class cv_image():
    def __init__(self, image_path):
        self.image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY) # Read for gray-scale
        self.arti_image = self.image.copy()

    def mean_filter(self): # 3x3 filter
        
        pad_image = cv2.copyMakeBorder(self.arti_image, 1, 1, 1, 1, cv2.BORDER_REFLECT) # Padding image with the reflect pixel for 1

        for i in range(self.arti_image.shape[0]):
            for j in range(self.arti_image.shape[1]):
                self.arti_image[i][j] = 1.0 / 9.0 * (pad_image[i:i+3, j:j+3].sum()) # Mean the window values

    def USM(self):
        self.arti_image = 0.8*(self.image - self.arti_image)/255 + self.image

    def pepper_noise(self): # 15% pepper noise
        num_pepper = 0.15 * self.arti_image.size
        while(num_pepper > 0): # Use while to spill the pepper when the number of pepper to zero
            for i in range(self.arti_image.shape[0]):
                for j in range(self.arti_image.shape[1]):
                    if(random.randint(0, 100) > 90): # only 10% can spill the pepper
                        if(num_pepper == 0):
                            break
                        self.arti_image[i][j] = 255 # Spill pepper
                        num_pepper = num_pepper - 1 # Number of pepper - 1

    def median_filter(self):
        pad_image = cv2.copyMakeBorder(self.arti_image, 1, 1, 1, 1, cv2.BORDER_REFLECT) # Padding image with the reflect pixel for 1

        for i in range(self.arti_image.shape[0]):
            for j in range(self.arti_image.shape[1]):
                self.arti_image[i][j] = np.sort(pad_image[i:i+3, j:j+3].flatten())[4] # Get the center sort value of windows