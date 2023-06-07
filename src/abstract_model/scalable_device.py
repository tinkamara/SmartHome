from abc import abstractmethod
from abstract_model.device import device


class scalable_device(device):

    @abstractmethod
    def scale_device(self, value):
        pass