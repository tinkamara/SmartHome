from model.smart_devices.smart_device import SmartDevice


class SwitchLight(SmartDevice):
    type_name = "Light (on/off)"

    def __init__(self, name, brand="Osram", model="LED-Lampe Glühlampenform E27 klar", is_on=False):
        super().__init__(name, self.get_type())
        self.brand = brand
        self.model = model
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print("The light has been turned on.")

    def turn_off(self):
        self.is_on = False
        print("The light has been turned off.")
