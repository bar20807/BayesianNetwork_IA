"""
    Universidad del Valle de Guatemala
    José Rodrigo Barrera García
    20807
    Laboratorio 2 - Redes Bayesianas
"""

import pathlib
from setuptools import find_packages, setup
from BayesianNetwork import __version__

HERE = pathlib.Path(__file__).parent

VERSION = {}
with open(HERE / "BayesianNetwork" / "version.py") as fp:
    exec(fp.read(), VERSION)
PACKAGE_NAME = "BayesianNetwork"
AUTHOR = "José Rodrigo Barrera García"
AUTHOR_EMAIL = "bar20807@uvg.edu.gt"
URL = "https://github.com/bar20807/BayesianNetwork_IA"

LICENSE = "MIT"  # Tipo de licencia
DESCRIPTION = (
    "Permite el manejo y construccion de Redes Bayesianas"  # Descripción corta
)

LONG_DESCRIPTION = (HERE / "README.md").read_text(
    encoding="utf-8"
)  # Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


# Paquetes necesarios para que funcione la libreía. Se instalarán en el caso de que no esten instalados
INSTALL_REQUIRES = ["build"]

KEYWORDS = ["bayesian-networks", "artificial-intelligence", "machine-learning"]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
]

setup(
    name=PACKAGE_NAME,
    version=VERSION["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
)