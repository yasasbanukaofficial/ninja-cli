from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text
from rich import box
from ninjacli.ui.logo import get_logo_text 

def header_display(console: Console | None = None):
    console = console or Console()

    logo_text = get_logo_text()
    info_text = Text("\nWelcome to Ninja CLI! Ready to code?\n", style="bold white", justify="center")
    author_text = Text.assemble(
        ("@yasasbanukaofficial", "bold cyan"),
        " - GitHub, NPM | ",
        ("@yasasbanukagunasena", "bold magenta"),
        " - LinkedIn | ",
        ("Yasas Banu", "bold red"),
        " - Google Me\n",
        style="bold white",
        justify="center"
    )

    header = Group(logo_text, info_text, author_text)
    rules_set = Group(
        Text("To get the best output:", style="bold white"),
        Text.assemble("1. Enter prompt in a", (" structured format.", "red"), style="bold white"),
        Text.assemble("2. Use", (" SHIFT + ENTER ", "blue") ,"for a new line", style="bold white"),
        Text.assemble("2. For more information use", (" #help ", "magenta"), style="bold white"),
    )
    header_panel = Panel(
        rules_set,
        title="[bold #00FFAA]NINJA CLI[/bold #00FFAA]",
        border_style="#00FFAA",
        padding=(1, 2),
        box=box.DOUBLE,
    )

    console.clear()
    console.print("\n", header)
    console.print(header_panel, "\n")
    

header_display()
