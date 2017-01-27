from setuptools import setup

setup(
    name = "rysize",
    version = "0.4.1",
    description = "CLI application for bulk resizing of images",
    url = "https://github.com/nechoventsi/rysize",
    author = "Ventsislav Dimitrov",
    license = "MIT",
    py_modules = ["rysize"],
    install_requires = [
        "Click>=6.6",
        "Pillow>=3.3.1"],
    entry_points = '''
        [console_scripts]
        rysize=rysize:rysize
    ''',
)