# Color Image Processing Homework 1

> Author: Skyler Chen

> Date: 2022/10/22

[TOC]

## Intorduction

In this homework, I choose equation 2 and euqation 3 for my anser experiment.

## Coding Detail

### Envionment
We use Python environment by version 3.8, and use cv2, numpy to achieve the equation.

### utils.py

I package all function in the cv_image class.

```python
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
```

### Equation 2

```python
import config
import utils
import cv2

if __name__ == "__main__":
    IMAGE_PATH = config.IMAGE_PATH
    image = utils.cv_image(IMAGE_PATH)

    image.mean_filter()
    cv2.imwrite("mean_filter.png", image.arti_image)
    image.USM()
    cv2.imwrite("USM.png", image.arti_image)
```
1. I use mean filter to blur the orignal image.
2. Use Origianl image minus Blur image and normalization to [0,1]. Multiply a scale factor by 0.8 and plus the original image.

<p float="left">
<img src=".\ntust_gray.jpg" alt="drawing" width="200"/>
<img src=".\mean_filter.png" alt="drawing" width="200"/>
<img src=".\USM.png" alt="drawing" width="200"/>
</p>

### Equation 3

```python
import config
import utils
import cv2

if __name__ == "__main__":
    IMAGE_PATH = config.IMAGE_PATH
    image = utils.cv_image(IMAGE_PATH)
    image.pepper_noise()
    cv2.imwrite("pepper.png", image.arti_image)
    image.median_filter()
    cv2.imwrite("median_filter.png", image.arti_image)
```
1. I use a while loop to spill the pepper for 15% of image size and use 10% to spill the pepper.
2. Flatten the window array to 1-D, and sort and take the median value to replace the center one.

<p float="left">
<img src=".\ntust_gray.jpg" alt="drawing" width="200"/>
<img src=".\pepper.png" alt="drawing" width="200"/>
<img src=".\median_filter.png" alt="drawing" width="200"/>
</p>