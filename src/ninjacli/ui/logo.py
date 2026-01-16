from rich.console import Console
from rich.text import Text

LOGO_ART = """
 ███    ██ ██ ███    ██      ██  █████        ██████ ██      ██ 
 ████   ██ ██ ████   ██      ██ ██   ██      ██      ██      ██ 
 ██ ██  ██ ██ ██ ██  ██      ██ ███████      ██      ██      ██ 
 ██  ██ ██ ██ ██  ██ ██ ██   ██ ██   ██      ██      ██      ██ 
 ██   ████ ██ ██   ████  █████  ██   ██       ██████ ███████ ██ 
"""

def print_colored_logo(ascii_text, start_hex="#f553bc", end_hex="#f85252"):
    console = Console()
    lines = ascii_text.splitlines()

    def mix_color(percent, start, end):
        s = [int(start[i:i+2], 16) for i in (1, 3, 5)]
        e = [int(end[i:i+2], 16) for i in (1, 3, 5)]
        mixed = [int(s[j] + (e[j] - s[j]) * percent) for j in range(3)]
        return f"#{mixed[0]:02x}{mixed[1]:02x}{mixed[2]:02x}"

    for line in lines:
        styled_line = Text()
        width = len(line)
        
        for i, char in enumerate(line):
            if char.isspace():
                styled_line.append(char)
            else:
                percent = i / width if width > 0 else 0
                color = mix_color(percent, start_hex, end_hex)
                styled_line.append(char, style=f"bold {color}")
        
        console.print(styled_line)

print_colored_logo(LOGO_ART)