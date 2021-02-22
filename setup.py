from distutils.core import setup
from setuptools import find_packages, setup
from pathlib import Path

HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name = 'htmlfactory',         # How you named your package folder (MyLib)
    packages = find_packages(exclude=("tests",)),
    version = '0.0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'A simple way to produce HTML with Python.',   # Give a short description about your library
    author = 'Jeff Gruenbaum',                   # Type in your name
    author_email = 'jeff.gruenbaum@gmail.com',      # Type in your E-Mail
    long_description=README,
    long_description_content_type="text/markdown",
    url = 'https://github.com/jgrugru/htmlfactory',   # Provide either the link to your github or to your website
    keywords = ["html", "template", "templating", "xml", "document", "form", "rendering"],
    install_requires=[
        "beautifulsoup4>=2.2",
    ],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)