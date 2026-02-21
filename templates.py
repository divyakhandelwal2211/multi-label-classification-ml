import os


PROJECT_NAME = "multi_label_ml_project"

FOLDERS = [
    f"{PROJECT_NAME}/data",
    f"{PROJECT_NAME}/src",
    f"{PROJECT_NAME}/models"
]

FILES = [
    f"{PROJECT_NAME}/src/__init__.py",
    f"{PROJECT_NAME}/src/data_loader.py",
    f"{PROJECT_NAME}/src/preprocessing.py",
    f"{PROJECT_NAME}/src/model.py",
    f"{PROJECT_NAME}/src/evaluate.py",
    f"{PROJECT_NAME}/main.py",
    f"{PROJECT_NAME}/requirements.txt",
    f"{PROJECT_NAME}/README.md"
]


def create_structure():
    
    # Create folders
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        print(f"Folder created: {folder}")

    # Create files
    for file in FILES:
        with open(file, "w") as f:
            pass
        print(f"File created: {file}")


if __name__ == "__main__":
    create_structure()