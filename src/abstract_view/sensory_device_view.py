from abc import abstractmethod
from abstract_view.device_view import device_view


class sensory_device_view(device_view):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass
