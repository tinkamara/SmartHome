from src.model.smart_devices.dimmable_light import DimmableLight
from src.model.smart_devices.fan import Fan
from src.model.smart_devices.switch_light import SwitchLight
from src.model.smart_devices.television import Television
from src.model.smart_spaces.smart_space import SmartSpace


class Room(SmartSpace):
    available_devices = [
        SwitchLight,
        DimmableLight,
        Fan,
        Television
    ]
    available_device_dict = {d.type_name: d for d in sorted(available_devices, key=lambda x: x.type_name)}

    def __init__(self, name, type="Room", temperature=25, humidity=50):
        super().__init__(name, type, temperature, humidity)
