

from setuptools import setup, find_packages
import codecs
import os

# here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Topsis Implimentation in Python'
# LONG_DESCRIPTION = 'Topsis Implimentation in Python'

# Setting up
setup(
    name="topsis-gurtaran-102003220",
    version=VERSION,
    author="Gurtaran Singh",
    author_email="<gurtaransingh01@gmail.com>",
    description=DESCRIPTION,
#     long_description_content_type="text/markdown",
#     long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'topsis', 'topsis implimentation'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
