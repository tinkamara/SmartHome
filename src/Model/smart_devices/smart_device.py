class SmartDevice:
    type_name = "Smart Device"

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_type(self):
        return self.type_name
