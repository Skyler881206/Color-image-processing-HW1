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