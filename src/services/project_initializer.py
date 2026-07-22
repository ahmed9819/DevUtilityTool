from src.services.project_creator import create_project
from src.services.git_service import init_git_repository

def initialize_project(project_name: str, initialize_git: bool=False):
    project_path = create_project(project_name)

    if initialize_git:
        init_git_repository(project_path)

    return project_path