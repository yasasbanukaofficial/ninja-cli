from ninjacli.cli.commands import create_file, read_file, update_file, delete_file, create_directory, read_directory, update_directory, delete_directory, build_project, run_project

available_tools = {
    "create_file": create_file,
    "read_file": read_file,
    "update_file": update_file,
    "delete_file": delete_file,
    "create_directory": create_directory,
    "read_directory": read_directory,
    "update_directory": update_directory,
    "delete_directory": delete_directory,
    "build_project": build_project,
    "run_project": run_project,
}