from abc import abstractmethod

from src.abstract_controller.device_controller import DeviceController


class SensoryDeviceController(DeviceController):
    
    @abstractmethod
    def process_user_input(self):
        pass