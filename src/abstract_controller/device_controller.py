from abc import ABC, abstractmethod


class device_controller(ABC):

    @abstractmethod
    def process_user_input(self):
        pass