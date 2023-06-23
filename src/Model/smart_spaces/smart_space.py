class SmartSpace:
    available_devices = []
    available_device_dict = dict()

    def __init__(self, name, type="Space", temperature=0, humidity=0):
        self.name = name
        self.type = type
        self.temperature = temperature
        self.humidity = humidity
        self.devices = []

    def get_available_device_dict(self):
        return self.available_device_dict

    def add_device(self, device_type, device_name):
        try:
            self.devices.append(device_type(device_name))
            return True
        except:
            return False
