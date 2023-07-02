import numpy as np


__all__ = [
    'center_crop'
]


def center_crop(image: np.ndarray, zoom: float) -> np.ndarray:
    if float(zoom) < 1.0:
        raise RuntimeError('Can\'t zoom out')

    if float(zoom) == 1.0:
        return image

    h, w = image.shape[:2]

    x_center = w // 2
    y_center = h // 2
    w_cropped = int(w / zoom)
    h_cropped = int(h / zoom)

    x_shifted = x_center - w_cropped // 2
    y_shifted = y_center - h_cropped // 2

    if (x_shifted + w_cropped) - x_shifted == 0:
        raise RuntimeError('Zoom is too large')

    if (y_shifted + h_cropped) - y_shifted == 0:
        raise RuntimeError('Zoom is too large')

    return image[y_shifted:y_shifted+h_cropped, x_shifted:x_shifted+w_cropped]
