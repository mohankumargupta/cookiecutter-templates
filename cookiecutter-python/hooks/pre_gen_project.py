import urllib.request
import zipfile
import os
from pathlib import Path
import sys

def download_github_repo_zip(owner, repo, branch='main'):
    """
    Download a GitHub repository as a zip file.
    
    :param owner: Owner of the repository
    :param repo: Repository name
    :param branch: Branch name (default is 'main')
    """
    url = f'https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip'
    zip_filename = f'{repo}-{branch}.zip'
    
    try:
        urllib.request.urlretrieve(url, zip_filename)
        print(f'Repo {repo} downloaded successfully as {zip_filename}')
    except Exception as e:
        print(f'Failed to download repo {repo}. Error: {e}')

# Example usage
#owner = 'octocat'  # Replace with the actual owner
#repo = 'Hello-World'  # Replace with the actual repo name
#branch = 'main'  # Replace with the desired branch
#download_github_repo_zip(owner, repo, branch)


def clone_github_repo():
    print("Cloning esphome github repo")
    # Construct the URL to get the repository information

    url = f"https://github.com/esphome/esphome/archive/refs/heads/dev.zip"
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
            #esphome_dir = Path("esphome-dev")

            #esphome_dir.joinpath("setup.cfg").unlink()
            #esphome_dir.joinpath("setup.py").unlink()
            esphome_dir.joinpath("pyproject.toml").unlink()            
    except Exception as e:
        print(f"Failed to clone repository: {e}")
        sys.exit(1)

if "{{ cookiecutter.project_template }}" == "esphomedev":
    clone_github_repo()
