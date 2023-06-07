from abc import abstractmethod
from abstract_controller.device_controller import device_controller


class scalable_device_controller(device_controller):

    @abstractmethod
    def process_user_input(self):
        pass