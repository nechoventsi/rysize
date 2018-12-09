from setuptools import setup

setup(
    name = "rysize",
    version = "0.5.0",
    description = "CLI application for bulk image resizing",
    long_description = open("README.md").read(),
    url = "https://github.com/nechoventsi/rysize",
    author = "Ventsislav V. Dimitrov",
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
