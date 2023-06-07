from abc import abstractmethod
from src.abstract_model.device import Device


class BinaryDevice(Device):
    

    @abstractmethod
    def turn_on(self):
         pass
        
    @abstractmethod
    def turn_off(self):
        pass
