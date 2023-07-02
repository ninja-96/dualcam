from __future__ import annotations
from typing import Union, Tuple, List, Dict

import numpy as np
from picamera2 import Picamera2
from pydantic.dataclasses import dataclass

from dualcam.camera.base import BaseCamera


__all__ = [
    'RPICamera',
    'RPICameraBuilder',
    'RPICameraArgs',
    'RPICameraFactory'
]


class RPICamera(BaseCamera):
    def __init__(self, camera: Picamera2) -> None:
        self._camera = camera
        self._camera.start()

    def cap(self) -> np.ndarray:
        return self._camera.capture_array()

    def __del__(self) -> None:
        self._camera.close()


class RPICameraBuilder:
    def __init__(self) -> None:
        self._size = (1640, 1230)  # (1640, 1232)
        self._sensor_format = 'RGB888'
        self._fps = 30

    def size(self, size: Union[List[int], Tuple[int]]) -> RPICameraBuilder:
        if isinstance(size, (List, Tuple)):
            self._size = tuple(size)
            return self

        raise TypeError()

    def sensor_format(self, sensor_format: str) -> RPICameraBuilder:
        if isinstance(sensor_format, str):
            self._sensor_format = sensor_format
            return self

        raise TypeError()

    def fps(self, fps: int) -> RPICameraBuilder:
        if isinstance(fps, int):
            self._fps = fps
            return self

        raise TypeError()

    def build(self) -> RPICamera:
        picam2 = Picamera2()
        picam2.configure(
            picam2.create_video_configuration(
                {
                    'size': self._size,
                    'format': self._sensor_format
                }
            )
        )
        picam2.set_controls(
            {
                'FrameRate': self._fps
            }
        )

        return RPICamera(
            picam2
        )


@dataclass(frozen=True)
class RPICameraArgs:
    size: str
    sensor_format: str
    fps: int


class RPICameraFactory:
    @staticmethod
    def create(cfg: Dict) -> RPICamera:
        args = RPICameraArgs(**cfg)

        return RPICameraBuilder()\
            .size(args.size)\
            .sensor_format(args.sensor_format)\
            .fps(args.fps)\
            .build()
