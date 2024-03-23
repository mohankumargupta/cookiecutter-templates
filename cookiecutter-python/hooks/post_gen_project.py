from pathlib import Path
if "{{ cookiecutter.project_template }}" == "cli":
    Path('__init__.py').touch()