from model.smart_devices.smart_device import SmartDevice


class Television(SmartDevice):
    type_name = "Television"

    def __init__(self, name, brand="Sony", model="BRAVIA KD-55X80K LED TV", size_in_inches=55,
                 is_on=False, volume=50, channel=1):
        super().__init__(name, self.get_type())
        self.brand = brand
        self.model = model
        self.size = size_in_inches
        self.is_on = is_on
        self.volume = volume
        self.channel = channel

    def turn_on(self):
        self.is_on = True
        print("The television has been turned on.")

    def turn_off(self):
        self.is_on = False
        print("The television has been turned off.")

    def increase_volume(self):
        if self.is_on and self.volume < 100:
            self.volume += 1
            print("Volume increased:", self.volume)

    def decrease_volume(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1
            print("Volume decreased:", self.volume)

    def change_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print("Channel changed to", self.channel)
