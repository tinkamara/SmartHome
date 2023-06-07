from abc import abstractmethod
from abstract_model.device import device


class sensory_device(device):

    @abstractmethod
    def getValue(self, value):
        pass
