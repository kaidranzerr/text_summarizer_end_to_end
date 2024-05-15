import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]



# logic for creating the above files
for filepath in list_of_files:
    filepath = Path(filepath)
    # seperate the files and folders so we can create them individually
    filedir , filename = os.path.split(filepath)

    # checking if file directory is not empty
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # now for file creation first check that this file doesn't exists already 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , 'w') as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists!!!")










# Path will first detect the operating system and based on that it will provide the path
# params.yaml will contain all model related parameters
# pipeline folder will contain our training and prediction pipeline
# inside the common file we write our all the utilities
# .github folder is created to do real time deployment changes when new code is commited and there we will write our yaml file 
# and also related to ci/cd stuff
# logic for folder structure generation
# constructor file is needed because we need to install that src stuff as a local package 

# whenever we are creating a new project do create a virtual enviorment first

