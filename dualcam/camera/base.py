from abc import ABCMeta, abstractmethod

import numpy as np


class BaseCamera(metaclass=ABCMeta):
    @abstractmethod
    def cap(self) -> np.ndarray:
        pass
