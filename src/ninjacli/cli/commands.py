import subprocess, shlex, os

FORBIDDEN_CMDS = {"rm", "del", "format", "sudo", "chmod", "chown"}
EXIT_COMMANDS = {"exit", "quit", "bye", "stop", "leave", "ctrl+c"}

def execute_safely(cmd_str: str, allow_delete: bool = False):
    """
       Common method for executing commands
    """
    args = shlex.split(cmd_str)
    
    if not args:
        return "No command provided"
    
    if args[0].lower() in FORBIDDEN_CMDS:
        return f"Access Denied: {args[0]} is a restricted command."
    
    try: 
        # result =  subprocess.run(args, capture_output=True, text=True, timeout=30)
        # return {
        #     "command": cmd_str,
        #     "return_code": result.returncode,
        #     "stdout": result.stdout.strip(),
        #     "stderr": result.stderr.strip()
        # }
        return os.system(cmd_str)
    except Exception as e:
        return str(e)
    

def create_file(cmd_str: str):
    """ 
        This command creates a file
    """ 
    return execute_safely(cmd_str)

def read_file(cmd_str: str):
    """
        This command reads a file
    """
    return execute_safely(cmd_str)

def update_file(cmd_str: str):
    """
        This command updates a file
    """
    return execute_safely(cmd_str)

def delete_file(cmd_str: str):
    """
        This command deletes a file
    """
    return execute_safely(cmd_str, allow_delete=True)

def create_directory(cmd_str: str):
    """
        This command creates a directory
    """
    return execute_safely(cmd_str)

def read_directory(cmd_str: str):
    """
        This command lists contents of a directory
    """
    return execute_safely(cmd_str)

def update_directory(cmd_str: str):
    """
        This command updates a directory (e.g., renames it)
    """
    return execute_safely(cmd_str)

def directory_exists(cmd_str: str):
    """
        This command checks if a directory exists
    """
    dir_path = shlex.split(cmd_str)[-1] if shlex.split(cmd_str) else ""
    if not dir_path:
        return "No directory path provided"
    return os.path.isdir(dir_path)

def file_exists(cmd_str: str):
    """
        This command checks if a file exists
    """
    file_path = shlex.split(cmd_str)[-1] if shlex.split(cmd_str) else ""
    if not file_path:
        return "No file path provided"
    return os.path.isfile(file_path)

def delete_directory(cmd_str: str):
    """
        This command deletes a directory
    """
    return execute_safely(cmd_str, allow_delete=True)


def run_project(cmd_str: str):
        """
            This command runs a project
        """
        return execute_safely(cmd_str)

def build_project(cmd_str: str):
        """
            This command builds a project
        """
        return execute_safely(cmd_str)
    