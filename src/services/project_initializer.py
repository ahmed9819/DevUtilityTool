from src.services.project_creator import create_project
from src.services.git_service import init_git_repository
from src.services.venv_service import create_virtual_environment
from src.services.template_service import apply_template

def initialize_project(
        project_name: str,
        initialize_git: bool=False, 
        initialize_venv: bool=False, 
        template_name="default"
    ):
    
    project_path = create_project(project_name)
    apply_template(project_path ,template_name)

    if initialize_git:
        init_git_repository(project_path)

    if initialize_venv:
        create_virtual_environment(project_path)

    return project_path