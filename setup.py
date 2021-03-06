#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from sales.__init__ import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from sales/__init__.py"""
    version_match = __version__
    if version_match:
        return version_match
    raise RuntimeError("Unable to find version string.")


version = get_version("sales", "__init__.py")


if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print("Wheel library missing. Please run 'pip install wheel'")
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
requirements = open("requirements.txt").readlines()

setup(
    name="pharmcrm2-sales",
    version=version,
    description="""PharmCRM2 Sales""",
    long_description=readme + "\n\n" + history,
    author="Pavel Tanchev",
    author_email="dcopm999@gmail.com",
    url="https://github.com/dcopm999/pharmcrm2-sales",
    packages=[
        "sales",
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="pharmcrm2-sales",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
