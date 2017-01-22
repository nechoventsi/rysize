import os
import PIL
from PIL import Image
import click

imgExts = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

@click.command()
@click.option("-p", "--path", prompt="Directory", help="Full path to containing directory or file. Use '.' for current working directory.")
@click.option("-w", "--width", type=int, help="New width.")
@click.option("-h", "--height", type=int, help="New height.")
@click.option("-r", "--ratio", default=1.0, help="Percentage of original size.")
@click.version_option()

def rysize(path, width, height, ratio):
    
    """Command-line interface application for bulk resizing of images in a given directory. Build with Python.
    
    More info: https://github.com/nechoventsi/rysize"""
    
    if os.path.isdir(path) == True:
        files = os.listdir(path)

    elif path == ".":
        files = os.listdir(os.getcwd())
        path = os.getcwd()

    elif os.path.isfile(path) == True:
        files = [os.path.basename(path)]
        path = os.path.dirname(path)

    with click.progressbar(files, label="Resizing...") as bar:
        for fname in bar:

            fnameParts = os.path.splitext(fname)
            if fnameParts[1].lower() not in imgExts:
                continue

            filePath = os.path.join(path, fname)
            img = Image.open(filePath)

            if width:

                widthPercent = (width/float(img.size[0]))
                height = int((float(img.size[1])*float(widthPercent)))
            
            elif height:

                heightPercent = (height/float(img.size[1]))
                width = int((float(img.size[0])*float(heightPercent)))

            elif ratio:

                width = int(ratio*img.size[0])
                height = int(ratio*img.size[1])

            imgNew = img.resize((width, height), PIL.Image.ANTIALIAS)

            pathParts = os.path.splitext(filePath)

            imgNew.save(pathParts[0] + "_resized" + pathParts[1])

    click.echo("Done!")

if __name__ == '__main__':
    rysize()