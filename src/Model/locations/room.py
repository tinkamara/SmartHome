class Room:
    def __init__(self):
        self.groups = []
        self.devices = []

    def add_group(self, group):
        self.groups.append(group)

    def add_device(self, device):
        self.devices.append(device)
