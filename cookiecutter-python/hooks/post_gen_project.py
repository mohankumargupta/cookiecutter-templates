from pathlib import Path
import shutil

if "{{ cookiecutter.project_template }}" == "cli":
    src = Path("src")
    src.mkdir()
    project = src.joinpath("{{ cookiecutter.project_name }}")
    project.mkdir()
    project.joinpath('__init__.py').touch()
    shutil.move("main.py", project)

if "{{ cookiecutter.project_template }}" == "cli":
    dest = Path("..")
    shutil.move("pyproject.toml", dest)
    shutil