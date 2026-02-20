import os 
from pathlib import Path
project_name='src'
list_of_files=[
    ".github/workflow/.getkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/pipeline/__init__/py",
    f"{project_name}/entity/__init.py",
    f"{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirenments.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filepath) or (os.path.getsize)):
        with open(filepath,"w") as f:
            pass