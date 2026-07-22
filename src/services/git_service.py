import subprocess

class GitNotInstalledError(Exception):
    pass

def init_git_repository(project_path):
    try:
        subprocess.run(
            ["git", "init"],
            cwd=project_path,
            check=True           
            )
        
        subprocess.run(
            ["git", "branch",  "-M",  "main"],
            cwd=project_path,
            check=True
        )

    except FileNotFoundError:
        raise GitNotInstalledError(
            "Git is not installed or not available in PATH."
        )

