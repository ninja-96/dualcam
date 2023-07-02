from setuptools import find_packages, setup
import dualcam


with open("LICENSE", "r", encoding='utf-8') as fh:
    licence = fh.read()


setup(
    name='Dualcam',
    version=dualcam.__version__,
    description='Narrow and telephoto images from one high definition image from RPI camera',
    author='Oleg Kachalov',
    packages=find_packages(),
    python_requires='>=3.9'
)
