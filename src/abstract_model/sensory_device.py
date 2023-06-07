from abc import abstractmethod

from src.abstract_model.device import Device


class SensoryDevice(Device):

    @abstractmethod
    def get_value(self, value):
        pass
