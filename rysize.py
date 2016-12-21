import os
import PIL
from PIL import Image
import click

imgExts = ["png", "jpg", "bmp", "fit", "gif"]

@click.command()
@click.option("-p", "--path", prompt="Directory", help="Full path to containing directory.")
@click.option("-w", "--width", type=int, help="New width of file.")
@click.option("-h", "--height", type=int, help="New height of file.")
@click.option("-r", "--ratio", default=1.0, help="Percentage of original size.")
@click.version_option()

def rysize(path, width, height, ratio):
    
    """Command-line interface application for bulk resizing of images in a given directory. Build with Python."""
    
    with click.progressbar(os.listdir(path), label="Resizing...") as bar:
        for fname in bar:

            ext = fname[-3:].lower()
            if ext not in imgExts:
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

            imgNew.save(filePath[:-4]+"_resized"+filePath[-4:])

    click.echo("Done!")

if __name__ == '__main__':
    rysize()