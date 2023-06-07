from abc import abstractmethod
from src.abstract_model.device import Device


class ScalableDevice(Device):

    @abstractmethod
    def scale_device(self, value):
        pass