from src.controller.scalable_light_controller import scalable_light_controller
from src.model.scalable_light import scalable_light
from src.view.scalable_light_view import scalable_light_view


def main():

    light = scalable_light()
    view = scalable_light_view(light)
    controller = scalable_light_controller(light, view)

    
    while True:
        view.display()
        controller.process_user_input()


if __name__ == "__main__":
    main()