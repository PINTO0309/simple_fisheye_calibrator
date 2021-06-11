from setuptools import setup, Extension
from setuptools import find_packages
from os import listdir

with open("README.md") as f:
    long_description = f.read()

scripts = ["scripts/"+i for i in listdir("scripts")]

def _requires_from_file(filename):
    return open(filename).read().splitlines()

if __name__ == "__main__":
    setup(
        name="simple_fisheye_calibrator",
        scripts=scripts,
        version="0.0.9",
        description="Simple GUI-based correction of fisheye images. The correction parameters specified on the screen can be diverted to opencv's fisheye correction parameters.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Katsuya Hyodo",
        author_email="rmsdh122@yahoo.co.jp",
        url="https://github.com/PINTO0309/simple_fisheye_calibrator",
        license="MIT License",
        packages=find_packages(),
        platforms=["linux", "unix"],
        python_requires=">3.6",
        install_requires=_requires_from_file('requirements.txt'),
    )
