from abc import abstractmethod
from AbstractModel.Device import Device


class BinaryDevice(Device) :
    

    @abstractmethod
    def turn_on(self):
         pass
        
    @abstractmethod
    def turn_off(self):
        pass
