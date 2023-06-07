from abc import abstractmethod
from src.abstract_view.device_view import DeviceView


class BinaryDeviceView(DeviceView):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass
