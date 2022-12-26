from setuptools import setup
import sys
if sys.version_info >= (3,7):
    sys.exit('Sorry, Python > 3.7 is not supported, this is due to the mode pywin32 is not fully support for python 3.7 or above')
setup()
