from __future__ import annotations
from typing import Union, Tuple, List, Dict

import cv2
import numpy as np
from pydantic.dataclasses import dataclass

from dualcam.camera.base import BaseCamera


__all__ = [
    'CVCamera',
    'CVCameraBuilder',
    'CVCameraArgs',
    'CVCameraFactory'
]


class CVCamera(BaseCamera):
    def __init__(self, camera: cv2.VideoCapture) -> None:
        self._camera = camera

    def cap(self) -> np.ndarray:
        ret, image = self._camera.read()
        if ret:
            return image

        raise RuntimeError()


class CVCameraBuilder:
    def __init__(self) -> None:
        self._source = None

    def source(self, source: Union[int, str]) -> CVCameraBuilder:
        if isinstance(source, (int, str)):
            self._source = source
            return self

        raise TypeError()

    def build(self) -> CVCamera:
        cap = cv2.VideoCapture(self._source)

        return CVCamera(
            cap
        )


@dataclass(frozen=True)
class CVCameraArgs:
    source: Union[int, str]


class CVCameraFactory:
    @staticmethod
    def create(cfg: Dict) -> CVCamera:
        args = CVCameraArgs(**cfg)

        return CVCameraBuilder()\
            .source(args.source)\
            .build()
