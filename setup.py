from setuptools import setup

setup(
    name="rysize",
    version="0.1",
    py_modules=["rysize"],
    install_requires=[
        "Click", "Pillow"],
    entry_points='''
        [console_scripts]
        rysize=rysize:rysize
    ''',
)