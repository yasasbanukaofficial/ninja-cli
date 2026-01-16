from rich.console import Console
from rich.text import Text

LOGO_ART = """
 ███    ██ ██ ███    ██      ██  █████        ██████ ██      ██ 
 ████   ██ ██ ████   ██      ██ ██   ██      ██      ██      ██ 
 ██ ██  ██ ██ ██ ██  ██      ██ ███████      ██      ██      ██ 
 ██  ██ ██ ██ ██  ██ ██ ██   ██ ██   ██      ██      ██      ██ 
 ██   ████ ██ ██   ████  █████  ██   ██       ██████ ███████ ██ 
"""

def print_simple_logo():
    console = Console()
    
    colors = [
    "#f553bc",  
    "#f34bb3",  
    "#f0429a",  
    "#e83a7a",  
    "#d92f5a",  
]
    
    lines = LOGO_ART.splitlines()
    for i, line in enumerate(lines):
        color_index = min(i, len(colors) - 1)
        console.print(line, style=f"bold {colors[color_index]}")

print_simple_logo()