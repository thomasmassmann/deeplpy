# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deeplpy",
    version="0.1",
    author="Thomas Massmann",
    author_email="thomas.massmann@it-spir.it",
    description="Translate source strings with deepL.",
    install_requires=["requests"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmassman/deeplpy",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
