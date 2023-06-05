from abc import abstractmethod
from AbstractController.DeviceController import DeviceController


class ScalableDeviceController(DeviceController):

    @abstractmethod
    def process_user_input(self):
        pass