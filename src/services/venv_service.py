import subprocess
import sys

class VirtualEnvironmentCreationError(Exception):
    pass

def create_virtual_environment(project_path, venv_name=".venv"):
    try:
        subprocess.run(
            [
            sys.executable,
            "-m",
            "venv",
            venv_name
            ],
            cwd=project_path,
            check=True
        )
    except subprocess.CalledProcessError:
        raise VirtualEnvironmentCreationError(
            "Failed to create Virtual Environment."
        )
