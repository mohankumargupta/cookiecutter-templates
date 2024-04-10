import urllib.request
import zipfile
import os
from pathlib import Path

def clone_github_repo():
    print("Cloning esphome github repo")
    # Construct the URL to get the repository information
    url = f"https://github.com/esphome/esphome/archive/dev.zip"
    destination = Path(".")
    try:
        # Download the repository content as a zip file
        with urllib.request.urlopen(url) as response:
            # Create the destination directory if it doesn't exist
            os.makedirs(destination, exist_ok=True)

            # Save the content to a temporary file
            temp_file_path = os.path.join(destination, 'temp.zip')
            with open(temp_file_path, 'wb') as f:
                f.write(response.read())

            # Extract the zip file
            with zipfile.ZipFile(temp_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination)

            print("Repository cloned successfully!")
            Path("temp.zip").unlink()
            esphome_dir = Path("esphome-dev")
            if esphome_dir.exists():
                esphome_dir.joinpath("setup.cfg").unlink()
                esphome_dir.joinpath("setup.py").unlink()
    except Exception as e:
        print(f"Failed to clone repository: {e}")

if "{{ cookiecutter.project_template }}" == "esphomedev":
    clone_github_repo()
