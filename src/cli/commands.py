import subprocess
import shlex

FORBIDDEN_CMDS = {"rm", "del", "format", "sudo", "chmod", "chown"}

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
        return subprocess.run(args, capture_output=True, text=True, timeout=30)
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

def delete_directory(cmd_str: str):
    """
        This command deletes a directory
    """
    return execute_safely(cmd_str, allow_delete=True)