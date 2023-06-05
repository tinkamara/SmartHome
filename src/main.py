
from View.LightView import LightView
from Model.ScalableLight import ScalableLight
from Controller.LightController import LightController



def main():

    light = ScalableLight()
    view = LightView(light)
    controller = LightController(light, view)

    
    while True:
        view.display_status()
        controller.process_user_input()


if __name__ == "__main__":
    main()