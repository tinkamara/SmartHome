from abc import ABC, abstractmethod


class DeviceController(ABC):

    @abstractmethod
    def process_user_input(self):
        pass
