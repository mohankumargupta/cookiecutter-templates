from pathlib import Path
import shutil
import os

if "{{ cookiecutter.project_template }}" == "cli":
    src = Path("src")
    src.mkdir()
    project = src.joinpath("{{ cookiecutter.project_name }}")
    project.mkdir()
    project.joinpath('__init__.py').touch()
    shutil.move("main.py", project)

if "{{ cookiecutter.project_template }}" == "esphomedev":
    esphome_dir = Path("esphome-dev")
    print(list(filter(lambda y:y.is_file(), Path(".").iterdir())))
    print(esphome_dir.exists())
    esphome_dir.joinpath("main.py").unlink()
    shutil.move("pyproject.toml", esphome_dir)
    shutil.move(esphome_dir.joinpath("setup.cfg"), esphome_dir.joinpath("_setup.cfg"))
    shutil.move(esphome_dir.joinpath("setup.py"), esphome_dir.joinpath("_setup.py"))
    os.remove("main.py")