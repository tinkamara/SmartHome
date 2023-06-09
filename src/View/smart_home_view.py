import tkinter as tk

class SmartHomeView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.add_room_button = tk.Button(root, text="Add Room", command=self.controller.add_room)
        self.add_room_button.pack()

        self.room_frames = []

    def update_status(self):
        for frame in self.room_frames:
            frame.destroy()

        self.room_frames = []

        for room_index, room in enumerate(self.controller.rooms):
            room_frame = tk.LabelFrame(self.root, text="Room {}".format(room_index + 1))
            room_frame.pack(padx=10, pady=10)

            group_frames = []
            roomdevice_frames = []

            for device_index, device in enumerate(room.devices):
                device_frame = tk.Frame(room_frame)
                device_frame.pack(padx=5, pady=5)

                button = tk.Button(device_frame, text="Toggle Device {}".format(device_index + 1),
                                   command=lambda r=room_index, g=group_index,
                                                  d=device_index: self.controller.on_button_click(r, g, d))
                button.pack(side=tk.LEFT)

                scale = tk.Scale(device_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                 command=lambda value, r=room_index, g=group_index,
                                                d=device_index: self.controller.on_scale(r, g, d, value))
                scale.pack(side=tk.LEFT)

                roomdevice_frames.append(device_frame)

            for group_index, group in enumerate(room.groups):
                group_frame = tk.LabelFrame(room_frame, text="Group {}".format(group_index + 1))
                group_frame.pack(padx=10, pady=10)

                device_frames = []

                for device_index, device in enumerate(group.devices):
                    device_frame = tk.Frame(group_frame)
                    device_frame.pack(padx=5, pady=5)

                    button = tk.Button(device_frame, text="Toggle Device {}".format(device_index + 1),
                                       command=lambda r=room_index, g=group_index,
                                                      d=device_index: self.controller.on_button_click(r, g, d))
                    button.pack(side=tk.LEFT)

                    scale = tk.Scale(device_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                     command=lambda value, r=room_index, g=group_index,
                                                    d=device_index: self.controller.on_scale(r, g, d, value))
                    scale.pack(side=tk.LEFT)

                    device_frames.append(device_frame)

                group_frames.append(group_frame)

            self.room_frames.append(room_frame)
