from model.smart_devices.smart_device import SmartDevice


class Fan(SmartDevice):
    type_name = "Fan"

    def __init__(self, name, brand="DYSON", model="300912-01 AM 07 Turmventilator",
                 number_of_blades=0, is_on=False, speed=0):
        super().__init__(name, self.get_type())
        self.brand = brand
        self.model = model
        self.number_of_blades = number_of_blades
        self.is_on = is_on
        self.speed = speed

    def turn_on(self):
        self.is_on = True
        print("The fan has been turned on.")

    def turn_off(self):
        self.is_on = False
        print("The fan has been turned off.")

    def increase_speed(self):
        if self.is_on and self.speed < 3:
            self.speed += 1
            print("Speed increased:", self.speed)

    def decrease_speed(self):
        if self.is_on and self.speed > 0:
            self.speed -= 1
            print("Speed decreased:", self.speed)
