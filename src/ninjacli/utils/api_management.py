from ninjacli.cli.tools import create_file, update_file, file_exists

def is_api_saved(selected_option: str, api_key: str) -> bool:
    if not file_exists(".halo"):
        create_file(f'echo "API_KEY=\\"{api_key}\\"" > .halo')
        update_file(f'echo "API_OPTION=\\"{selected_option}\\"" >> .halo')
        return True
    return False
        