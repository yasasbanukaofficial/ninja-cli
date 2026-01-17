import os
import time
from rich.console import Console, Group, RenderableType
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich import box
from ninjacli.ui.logo import get_logo_text

console = Console()

def is_dir_root():
    cwd = os.getcwd()
    home = os.path.expanduser("~")
    return cwd == home

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
        Text.assemble("2. Use", (" SHIFT + ENTER ", "blue"), "for a new line", style="bold white"),
        Text.assemble("3. For best performance of this CLI, use", (" Linux or Mac ", "magenta"), style="bold white"),
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
    console.print(header_panel)          

    progress = Progress(
        SpinnerColumn(spinner_name="bouncingBall", style="bold magenta", speed=0.1),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=None, complete_style="bold #00FFAA", finished_style="bold green"),
        console=console,
        transient=True,
    )
    task = progress.add_task("Checking directories...", total=100)

    def make_panel() -> RenderableType:
        return Panel(
            progress,  
            title="[bold #00FFAA]Loading[/bold #00FFAA]",
            border_style="#FF00AA",
            padding=(1, 2),
            box=box.ROUNDED
        )

    with Live(make_panel(), console=console, refresh_per_second=30, transient=True):
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.02)

    if is_dir_root():
        dir_panel = Panel(
            Text(
                "• You are running Ninja CLI in your root directory! Consider running it in a project directory for security.",
                style="bold white"
            ),
            title="[bold red]CAUTION[/bold red]",
            border_style="#FF006F",
            padding=(1, 2)
        )
        console.print(dir_panel)
    else:
        dir_panel = Panel(
            Text(
                "• Directory check passed!.",
                style="bold white"
            ),
            border_style="#FF006F",
        )
        console.print(dir_panel)

header_display()
