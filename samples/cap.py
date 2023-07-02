import cv2

from dualcam.camera.rpi_camera import RPICameraBuilder
from dualcam.dualcam import DualCamBuilder


if __name__ == '__main__':
    camera = RPICameraBuilder()\
        .build()

    dualcam = DualCamBuilder()\
        .build()

    while True:
        hires_image = camera.cap()
        narrow_image, tele_image = dualcam(hires_image)

        print(narrow_image.shape, tele_image.shape)
        cv2.imshow('Narrow', narrow_image)
        cv2.imshow('Tele', tele_image)
        k = cv2.waitKey(1)
        if k == 113:
            break
