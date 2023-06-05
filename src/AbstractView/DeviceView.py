from abc import ABC, abstractmethod


class DeviceView(ABC):
    

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass
