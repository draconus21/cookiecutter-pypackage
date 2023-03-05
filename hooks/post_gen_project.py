#!/usr/bin/env python
import os
import shutil
import fnmatch

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirname):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirname))


dirs_to_remove = [".vscode", ".undo"]
files_to_remove = ["Session.vim", "*.code-workspace"]


def isMatch(test, pattern_list):
    for patt in pattern_list:
        if fnmatch.fnmatch(test, patt):
            return True
    return False


if __name__ == "__main__":
    # remove files and directories that match  `files_to_remove` and `dirs_to_remove` respectively
    for f in os.listdir(PROJECT_DIRECTORY):
        if isMatch(f, files_to_remove):
            remove_file(f)
        elif isMatch(f, dirs_to_remove):
            remove_dir(f)

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.use_pypi_deployment_with_travis}}" != "y":
        remove_file(".travis.yml")
