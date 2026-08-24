from rich import print
from rich.panel import Panel
from rich.table import Table



print("[bold magenta]Hello[/bold magenta] [green]World[/green]!", ":vampire:", locals())

box = Panel("This is a box exemplifying the use of rich panels.", title="Rich Panel Example", subtitle="Enjoy!", style="bold blue")
print(box)

table = Table(title="Rich Table Example")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Price", style="magenta")
table.add_row("Apple", "$1.00")
table.add_row("Banana", "$0.50")
print(table)
