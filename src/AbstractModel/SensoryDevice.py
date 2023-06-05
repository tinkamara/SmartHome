from abc import abstractmethod
from AbstractModel.Device import Device


class SensoryDevice(Device):

    @abstractmethod
    def getValue(self, value):
        pass
