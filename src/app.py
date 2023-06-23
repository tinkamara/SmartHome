import tkinter as tk
from src.view.smart_home_app_view import SmartHomeAppView
from src.controller.smart_home_app_controller import SmartHomeAppController
from src.model.smart_home_model import SmartHomeModel


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Smart Home App')

        # create a model
        model = SmartHomeModel()

        # create a view and place it on the root window
        view = SmartHomeAppView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = SmartHomeAppController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
