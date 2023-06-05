
from View.ScalableLightView import ScalableLightView
from Model.ScalableLight import ScalableLight
from Controller.ScalableLightController import ScalableLightController



def main():

    light = ScalableLight()
    view = ScalableLightView(light)
    controller = ScalableLightController(light, view)

    
    while True:
        view.display()
        controller.process_user_input()


if __name__ == "__main__":
    main()