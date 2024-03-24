from pathlib import Path
import shutil

if "{{ cookiecutter.project_template }}" == "cli":
    Path("{{ cookiecutter.project_name }}").mkdir()
    Path("{{ cookiecutter.project_name }}").joinpath('__init__.py').touch()
    shutil.move("main.py", "{{ cookiecutter.project_name }}")