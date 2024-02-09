"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"

# constants
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = ROOT_DIR / "data"
EXP_DIR = ROOT_DIR / "experiments"
LOG_DIR = ROOT_DIR / "logs"
LOG_CFG = ROOT_DIR / "default-logging.json"

from {{ cookiecutter.project_slug }}.utils.logutils import setupLogging

setupLogging(
    console_level="INFO",
    root_level="INFO",
    log_cfg=LOG_CFG,
    log_dir=LOG_DIR,
)

del setupLogging
del utils
del Path
