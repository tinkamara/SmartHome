import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interface Example")

        self.new_device_id = 1
        self.devices = []

    def add_device(self, device):
        self.devices.append(device(self.new_device_id, self.root))
        self.new_device_id += 1

    def remove_device(self, device):
        self.devices.remove(device)

    def run(self):
        self.root.mainloop()
