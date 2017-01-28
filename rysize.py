import os
import PIL
from PIL import Image
import click

supported_image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

@click.command()
@click.option("-p", "--path", prompt="Directory", help="Full path to containing directory or file. Use '.' for current working directory. Does not recursively go through lower level directories.")
@click.option("-w", "--width", type=int, help="New width of file(s) in pixels.")
@click.option("-h", "--height", type=int, help="New height of file(s) in pixels.")
@click.option("-r", "--ratio", default=1.0, help="Percentage of original size.")
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

if __name__ == '__main__':
    rysize()