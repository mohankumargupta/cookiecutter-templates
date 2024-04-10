import urllib.request
import zipfile
import os

def clone_github_repo():
    print("Cloning esphome github repo")
    # Construct the URL to get the repository information
    url = f"https://github.com/esphome/esphome/archive/dev.zip"

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
                zip_ref.extractall(Path("."))

            print("Repository cloned successfully!")
    except Exception as e:
        print(f"Failed to clone repository: {e}")

if "{{ cookiecutter.project_template }}" == "esphomedev":
    clone_github_repo()
