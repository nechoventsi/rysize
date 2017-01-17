# rysize

*rysize* is a command-line interface application for bulk resizing of images. Build with Python, using [Click](http://click.pocoo.org/) and [Pillow](http://python-pillow.org/) (The friendly PIL fork).

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [To do](#to-do)
- [License](#license)

### Installation

I recommend installing *rysize* in a virtual environment, because I have not yet fully tested proper installation and automatic dependencies handling. The script is compatible with Python 2.7 *and* Python 3.5.

So download or clone the repo, start a new virtaulenv in its directory and install using setuptools:

    virtualenv -p python3 testenv
    . testenv/bin/activate
    python3 setup.py install

### Usage

In a terminal window simply do `rysize --help` to see the help page for the app. Options are:

    -p, --path TEXT       Full path to containing directory.
    -w, --width INTEGER   New width of file.
    -h, --height INTEGER  New height of file.
    -r, --ratio FLOAT     Percentage of original size.
    --version             Show the version and exit.
    --help                Show this message and exit.

An example resizing by width goes like this:

    rysize --width 800 /home/user/containing-folder

To check out functionallity without installation, try (note you'll have to have *Click* and *Pillow* installed):

    python rysize.py --width 800 /home/user/containing-folder

If the folder path isn't given, then *rysize* will prompt for it afterwards. No need to specify width *and* height simultaneously --- rysize maintains aspect ratio by default.

*rysize* currently handles **jpg**, **png**, **bmp** and **gif** file types. I have not yet implemented handling of images with extensions more than 3 characters long.

I have tested this on Linux only (Ubuntu). I would be glad if you try it out on different operating systems and tell me if it behaves properly. Feel free to open issues, etc.

### To do

:white_medium_small_square: More file types  
:white_medium_small_square: Test usage on Windows and macOS  
:white_medium_small_square: Possibility to resize only a single image with a given full path to file  
:white_medium_small_square: Watermarking...  

### License

MIT License

Copyright (c) 2016 Ventsislav Dimitrov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
