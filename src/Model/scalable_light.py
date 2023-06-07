from src.abstract_model import binary_device, scalable_device


class scalable_light(binary_device, scalable_device):
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def scale_device(self, brightness):
        self.brightness = brightness