from pathlib import Path
import shutil
class TemplateNotFoundError(Exception):
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = PROJECT_ROOT / "templates"


def apply_template(project_path, template_name="default"):

    """
    Copy the selected project template into the project directory.
    """

    template_path = TEMPLATE_DIR / template_name

    if not template_path.is_dir():
       raise TemplateNotFoundError(
            f"Template '{template_name}' does not exist."
        )

    
    shutil.copytree(template_path, project_path,dirs_exist_ok=True)