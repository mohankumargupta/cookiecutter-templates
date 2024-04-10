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
    vscode = Path(".vscode")
    vscode_launch = vscode.joinpath("launch.json")
    vscode_settings = vscode.joinpath("settings.json")
    vscode_dest = esphome_dir.joinpath(".vscode")
    Path("main.py").unlink()
    shutil.move("pyproject.toml", esphome_dir)
    shutil.move(vscode_launch, vscode_dest)
    shutil.move(vscode_settings, vscode_dest)
    shutil.rmtree(vscode)
    esphome_dir.joinpath("pytest.ini").unlink()
    