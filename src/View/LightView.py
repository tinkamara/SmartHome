class LightView:
    def __init__(self, light):
        self.light = light

    def display_status(self):
        if self.light.is_on:
            print("Light is on")
        else:
            print("Light is off")
        print("Brightness level:", self.light.brightness)

    def get_user_input(self):
        choice = input("Enter '1' to turn on the light, '2' to turn off, or '3' to set brightness: ")
        return choice