# Dualcam 

Narrow and telephoto images from one high definition image from Raspberry Pi camera.

## Installation

1. Install Raspberry Pi OS (Debian Bullseye 11 or higher) to your Rasberry Pi.
2. Install additional packages:
```bash
apt install python3-pyqt5 python3-opengl python3-picamera2
```

3. Install using `pip`\
From source:

```bash
pip3 install git+https://github.com/ninja-96/dualcam
```

## Getting Started

1. Import builder from library
```python
from dualcam.dualcam import DualCamBuilder
```

2. Build new instance
```python

dualcam = DualCamBuilder()\
    .build()
```

3. Push hires image to the instance
```python
narrow_image, tele_image = dualcam(hires_image)
```

To see more samples [here](./samples/)

## Built with

- [picamera2](https://github.com/raspberrypi/picamera2) - New libcamera based python library 
- [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library
## Versioning

All versions available, see the [tags on this repository](https://github.com/ninja-96/dualcam/tags).

## Authors

- **Oleg Kachalov** - _Initial work_ - [ninja-96](https://github.com/ninja-96)

See also the list of [contributors](https://github.com/ninja-96/dualcam/contributors) who participated in this project.

## License

This project is licensed under the GPL-3.0 license - see the [LICENSE.md](./LICENSE) file for details.
