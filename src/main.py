
import tkinter as tk

from src.controller.smart_home_controller import SmartHomeController
from src.view.smart_home_view import SmartHomeView


class SmartHome:
    def __init__(self):
        self.controller = SmartHomeController()

    def run(self):
        root = tk.Tk()
        view = SmartHomeView(root, self.controller)

        def update_gui():
            view.update_status()
            root.after(100, update_gui)

        update_gui()

        root.mainloop()

if __name__ == "__main__":
    gui = SmartHome()
    gui.run()
