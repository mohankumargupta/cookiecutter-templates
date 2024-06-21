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
    vscode_extensions = vscode.joinpath("extensions.json")
    vscode_tasks = vscode.joinpath("tasks.json")
    vscode_dest = esphome_dir.joinpath(".vscode")
    Path("main.py").unlink()
    shutil.move("pyproject.toml", esphome_dir)
    shutil.move(vscode_launch, vscode_dest)
    shutil.move(vscode_settings, vscode_dest)
    shutil.move(vscode_extensions, vscode_dest)
    shutil.move(vscode_tasks, vscode_dest)
    shutil.rmtree(vscode)
    #esphome_dir.joinpath("pytest.ini").unlink()
    #component_dir = esphome_dir / "esphome" / "components" / "{{ cookiecutter.project_name }}"
    component_dir = esphome_dir / "mohan" / "components" / "{{ cookiecutter.project_name }}"
    #print("about to mkdir")
    component_dir.mkdir(parents=True)
    #print("about to copy")
    shutil.copytree(src=Path("_extra_files").joinpath("esphomedev"), dst=component_dir, dirs_exist_ok=True)
    test_dir = esphome_dir / "tests" / "component_tests" / "{{ cookiecutter.project_name }}"
    mohan = esphome_dir / "mohan"
    shutil.copytree(src=Path("_extra_files").joinpath("esphomedevtest"), dst=mohan, dirs_exist_ok=True)

shutil.rmtree("_extra_files")
    