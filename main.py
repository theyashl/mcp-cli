import typer
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table

# Initialize Typer app
app = typer.Typer(help="MCP Installer CLI")
console = Console()

# Storage for our items
items = {}


@app.command()
def add():
    """
    Add a new item with multiple input steps
    """
    console.print(Panel.fit("[bold blue]Adding a new MCP Server[/bold blue]", border_style="blue"))

    # Multi-step input collection
    name = Prompt.ask("[green]Enter Server Name[/green]")
    url = Prompt.ask("[green]Enter Repository URL[/green]")
    cmd = Prompt.ask("[green]Enter Command[/green]")

    # Optional additional information
    add_args = Confirm.ask("[yellow]Add Command Args?[/yellow]")
    args = None
    if add_args:
        args = Prompt.ask("[green]Enter Command Args[/green]")

    add_envs = Confirm.ask("[yellow]Add Environment Variables?[/yellow]")
    envs = {}
    while add_envs:
        key = Prompt.ask("[green]Enter Environment Variable Key[/green]")
        description = Prompt.ask("[green]Enter Variable Description[/green]")
        add_default = Confirm.ask("[yellow]Add Default Value?[/yellow]")
        default = None
        if add_default:
            default = Prompt.ask(f"[green]Add Default Value for {key}[/green]")
        envs.update({
            key: {
                "desc": description,
                "default": default,
            }
        })
        add_envs = Confirm.ask("[yellow]Add More Environment Variables?[/yellow]")

    # Adding the item to our storage
    data = {
        name: {
            "repo": url,
            "cmd": cmd,
            "args": args,
            "envs": envs,
        }
    }

    global items
    items.update(data)

    # Success message with styled output
    console.print(Panel.fit(
        f"[bold green]Successfully added MCP Server:[/bold green]\n"
        f"[white]Name:[/white] {name}\n"
        f"[white]URL:[/white] {url}",
        border_style="green"
    ))


@app.command()
def list():
    """
    List all stored items
    """
    if not items:
        console.print("[yellow]No items found. Add some items first.[/yellow]")
        return

    table = Table(title="Stored Items")
    table.add_column("Name", style="cyan")
    table.add_column("URL", style="green")
    table.add_column("Data", style="yellow")

    for name, data in items:
        table.add_row(
            name,
            data["repo"],
            data
        )

    console.print(table)


@app.callback()
def main():
    """
    A beautiful MCP CLI tool
    """
    console.print("[bold blue]Welcome to the MCP CLI[/bold blue]")


if __name__ == "__main__":
    app()
