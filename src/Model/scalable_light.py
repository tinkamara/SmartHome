from src.abstract_model import binary_device, scalable_device
from src.abstract_model.binary_device import BinaryDevice
from src.abstract_model.scalable_device import ScalableDevice


class ScalableLight(BinaryDevice, ScalableDevice):
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def scale_device(self, brightness):
        self.brightness = brightness