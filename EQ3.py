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