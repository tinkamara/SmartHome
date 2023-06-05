from abc import abstractmethod
from AbstractModel.Device import Device


class ScalableDevice(Device):

    @abstractmethod
    def scale_device(self, value):
        pass