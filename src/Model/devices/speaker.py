from src.abstract_model.binary_device import BinaryDevice
from src.abstract_model.scalable_device import ScalableDevice
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer


class Speaker(BinaryDevice, ScalableDevice):
    def __init__(self):
        self.is_on = False
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def scale_device(self, volume):
        self.volume = volume
