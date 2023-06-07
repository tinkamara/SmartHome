from abc import ABC, abstractmethod


class device_view(ABC):
    

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass
