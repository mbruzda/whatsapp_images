import pywhatkit
import pathlib
import os


def send_image_to_number(phone_number, image_path):
    pywhatkit.sendwhats_image(phone_number, image_path, "Here is the image", 10, True, 5)


def read_all_images_in_directory(path):
    dir = pathlib.Path(path)
    return dir.iterdir()


def main():
    phone = "+48123456789" #tu numer telefonu z kierunkowym albo id grupy

    for image in read_all_images_in_directory("./images"):
        send_image_to_number(phone, image)
        os.remove(image)


if __name__ == "__main__":
    main()