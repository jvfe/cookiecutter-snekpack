#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("{{ cookiecutter.package_name }}")

if __name__ == "__main__":
    if "{{ cookiecutter.command_line_interface|lower }}" == "false":
        PACKAGE.joinpath("cli.py").unlink()
        PACKAGE.joinpath("__main__.py").unlink()
