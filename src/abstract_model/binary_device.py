from abc import abstractmethod
from abstract_model.device import device


class binary_device(device) :
    

    @abstractmethod
    def turn_on(self):
         pass
        
    @abstractmethod
    def turn_off(self):
        pass
