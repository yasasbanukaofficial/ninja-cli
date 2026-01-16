from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

def modern_prompt():
    console = Console()

    # 1. Create a stylized gradient header
    header_text = Text(" SYSTEM ACCESS ", style="bold white on #4e0303")
    
    # 2. Create the UI Panel for the question
    # We use a 'subtitle' for that small text effect at the bottom of the box
    message = Text("\nWelcome, Shinobi.\n", style="bold white")
    message.append("Identify yourself to initialize the session.", style="italic #8b0000")

    panel = Panel(
        message,
        title=header_text,
        title_align="left",
        border_style="#ff0e0e",
        padding=(1, 2),
        subtitle="[v0.24.0]",
        subtitle_align="right"
    )

    # Display the panel
    console.print("")
    console.print(panel)
    
    # 3. Modern Input Prompt
    # Using a custom 'choices_style' or just a clean arrow
    name = Prompt.ask(
        Text("> NAME", style="bold #ff0e0e"),
        default="Guest",
        console=console
    )

    console.print(f"\n[bold white]Access Granted.[/bold white] [italic #ff0e0e]Greetings, {name}.[/italic]\n")

if __name__ == "__main__":
    modern_prompt()