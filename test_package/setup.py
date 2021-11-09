from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='test_white_pouder',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    setup_requires=['requests', 'bs4'],
    url='https://github.com/zagidulin/Python_hw/tree/test_pack'
)