from abc import abstractmethod
from AbstractView.DeviceView import DeviceView


class SensoryDeviceView(DeviceView):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass
