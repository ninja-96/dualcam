from __future__ import annotations
from typing import Union, List, Tuple, Dict

import cv2
import numpy as np
from pydantic.dataclasses import dataclass

from dualcam.utils import center_crop


__all__ = [
    'DualCam',
    'DualCamBuilder'
    'DualCamArgs',
    'DualCamFactory'
]


class DualCam:
    def __init__(
        self,
        zoom: float,
        size: Union[List[int], Tuple[int]]
    ) -> None:
        self._zoom = zoom
        self._size = size

    def __call__(self, image: np.ndarray) -> np.ndarray:
        narrow = cv2.resize(
            image,
            tuple(self._size)
        )

        tele = cv2.resize(
            center_crop(
               image,
                self._zoom
            ),
            tuple(self._size)
        )

        return narrow, tele


class DualCamBuilder:
    def __init__(self) -> None:
        self._zoom = 3.0
        self._size = (640, 480)

    def zoom(self, scale: float) -> DualCamBuilder:
        if isinstance(scale, float):
            self._zoom = scale
            return self

        raise TypeError()

    def size(self, size: Union[List[int], Tuple[int]]) -> DualCamBuilder:
        if isinstance(size, (List, Tuple)):
            self._size = size
            return self

        raise TypeError()

    def build(self) -> DualCam:
        return DualCam(
            self._zoom,
            self._size
        )


@dataclass(frozen=True)
class DualCamArgs:
    zoom: float
    size: Union[List[int], Tuple[int]]


class DualCamFactory:
    @staticmethod
    def create(cfg: Dict) -> DualCam:
        args = DualCamArgs(**cfg)

        return DualCamBuilder()\
            .zoom(args.zoom)\
            .size(args.size)\
            .build()
