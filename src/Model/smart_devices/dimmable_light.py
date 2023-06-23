from model.smart_devices.smart_device import SmartDevice


class DimmableLight(SmartDevice):
    type_name = "Light (dimmable)"

    def __init__(self, name, brand="DELTACO GAMING", model="LED E27 smart Glühbirne Warmweiß",
                 is_on=False, brightness=0):
        super().__init__(name, self.get_type())
        self.brand = brand
        self.model = model
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True
        print("The light has been turned on.")

    def turn_off(self):
        self.is_on = False
        print("The light has been turned off.")

    def increase_brightness(self):
        if self.is_on and self.brightness < 100:
            self.brightness += 1
            print("Brightness increased:", self.brightness)

    def decrease_brightness(self):
        if self.is_on and self.brightness > 0:
            self.brightness -= 1
            print("Brightness decreased:", self.brightness)
