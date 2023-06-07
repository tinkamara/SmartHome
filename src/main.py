from src.controller.scalable_light_controller import ScalableLightController
from src.gui.gui import GUI
from src.model.scalable_light import ScalableLight
from src.view.scalable_light_view import ScalableLightView


def main():
    light = ScalableLight()
    view = ScalableLightView(light)
    controller = ScalableLightController(light, view)
    gui = GUI()
    gui.run()

    while True:
        view.display()
        controller.process_user_input()


if __name__ == "__main__":
    main()
