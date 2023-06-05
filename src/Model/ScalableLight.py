from AbstractModel.BinaryDevice import BinaryDevice
from AbstractModel.ScalableDevice import ScalableDevice


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