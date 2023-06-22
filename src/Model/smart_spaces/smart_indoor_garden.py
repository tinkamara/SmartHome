from model.smart_devices.dimmable_light import DimmableLight
from model.smart_devices.switch_light import SwitchLight
from model.smart_spaces.smart_space import SmartSpace


class SmartIndoorGarden(SmartSpace):
    available_devices = [
        SwitchLight,
        DimmableLight
    ]
    available_device_dict = {d.type_name: d for d in sorted(available_devices, key=lambda x: x.__name__)}

    def __init__(self, name, type="SIG", temperature=30, humidity=60):
        super().__init__(name, type, temperature, humidity)
