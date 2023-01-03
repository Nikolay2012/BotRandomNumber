import os

def downloads_images(name_file):
    path_img = os.path.join(os.path.abspath(__file__ + "/.."), name_file)
    with open(path_img, "rb") as file:
        img = file
    return img
