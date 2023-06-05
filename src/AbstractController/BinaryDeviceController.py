from abc import abstractmethod
from AbstractController.DeviceController import DeviceController


class BinaryDeviceController(DeviceController):

    @abstractmethod
    def process_user_input(self):
        pass