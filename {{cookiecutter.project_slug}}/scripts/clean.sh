#! /bin/bash

normal=$(tput sgr0)
red=$(tput setaf 1)
yellow=$(tput setaf 3)
green=$(tput setaf 2)

function green () {
    echo ${green}$1${normal}
}

function yellow() {
    echo ${yellow}$1${normal}
}

function red () {
    echo ${red}$1${normal}
}

green "═══ start {{ cookiecutter.project_slug }} clean.sh ═══"

if [[ -n "${{ '{' }}{{ cookiecutter.project_acronym }}_PYTHON_VENV}" ]]; then
    if [[ -d "${{ '{' }}{{ cookiecutter.project_acronym }}_PYTHON_VENV}" ]]; then
        green "removing ${{ '{' }}{{ cookiecutter.project_acronym }}_PYTHON_VENV}"
        rm -r "${{ '{' }}{{ cookiecutter.project_acronym }}_PYTHON_VENV}"/
    fi
fi

yellow "make sure to run source ./scripts/env.sh from a new terminal to setup the environment properly"

green "═══ end {{ cookiecutter.project_slug }} clean.sh ═══"