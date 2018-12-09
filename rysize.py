import os
import PIL
from PIL import Image
import click

supported_image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

path_help = """Full path to containing directory or file. The script does not recursively go through lower level directories, so it will handle only the images in the given directory.

Example: '--path /home/user/containing-folder'

Use '--path .' for current working directory. Can also resize only a single file by pointing to its destination, e.g. '--path /home/user/folder/example.jpg'."""

width_help = """New width of file(s). In pixels, defined by integer values. Maintains aspect ratio. Example: '--width 800'"""

height_help = """New height of file(s). In pixels, defined by integer values. Maintains aspect ratio. Example: '--height 800'"""

ratio_help = """Percentage of original size for the file(s). Use this if you want to scale pictures by a factor, given in floating-point numbers. Example: '--ratio 0.5' decreases the image size by 50%."""

@click.command()
@click.option("-p", "--path", prompt="Directory", help=path_help)
@click.option("-w", "--width", type=int, help=width_help)
@click.option("-h", "--height", type=int, help=height_help)
@click.option("-r", "--ratio", default=1.0, help=ratio_help)
@click.version_option()

def rysize(path, width, height, ratio):
    
    """Command-line interface application for bulk resizing of images in a given directory. Build with Python.
    
    More info: https://github.com/nechoventsi/rysize"""
    
    if os.path.isdir(path):
        files = os.listdir(path)
    elif path == ".":
        files = os.listdir(os.getcwd())
        path = os.getcwd()
    elif os.path.isfile(path):
        files = [os.path.basename(path)]
        path = os.path.dirname(path)

    with click.progressbar(files, label="Resizing...") as progress_bar:
        for file_name in progress_bar:
            extension = os.path.splitext(file_name)[1].lower()
            if extension not in supported_image_extensions:
                continue

            path_to_file = os.path.join(path, file_name)
            image = Image.open(path_to_file)

            if width:
                width_percentage = (width/float(image.size[0]))
                height = int((float(image.size[1])*float(width_percentage)))
            elif height:
                height_percentage = (height/float(image.size[1]))
                width = int((float(image.size[0])*float(height_percentage)))
            elif ratio:
                width = int(ratio*image.size[0])
                height = int(ratio*image.size[1])

            new_image = image.resize((width, height), PIL.Image.ANTIALIAS)
            path_to_file_parts = os.path.splitext(path_to_file)
            new_image.save(path_to_file_parts[0] + "_resized" + path_to_file_parts[1])

    click.echo("Done!")

if __name__ == "__main__":
    rysize()
