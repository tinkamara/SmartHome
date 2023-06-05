from AbstractController.BinaryDeviceController import BinaryDeviceController
from AbstractController.ScalableDeviceController import ScalableDeviceController


class ScalableLightController(BinaryDeviceController, ScalableDeviceController):
    def __init__(self, light, view):
        self.light = light
        self.view = view


    def process_user_input(self):
        choice = self.view.get_user_input()
        if choice == '1':
            self.light.turn_on()
        elif choice == '2':
            self.light.turn_off()
        elif choice == '3':
            brightness = int(input("Enter brightness level (0-100): "))
            self.light.scale_device(brightness)

        self.view.display()

        