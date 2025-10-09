from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

console.print("[bold yellow]Cast a spell:[/bold yellow]")
console.print("📜 - 1.[green]Expelliarmus[/green]")
console.print("📜 - 2.[green]Alohomora[/green]")
console.print("📜 - 3.[green]Avada Kedavra[/green]")
console.print("📜 - 4.[green]Protego[/green]")
console.print("📜 - 5.[green]Lumos[/green]")
console.print("📜 - 6.[green]Petrificus Totalus[/green]")

spell = Prompt.ask("[magenta]Which spell to cast?[/magenta]")
if (spell.lower() == "expelliarmus" or spell == "1"):
    console.print("[green]Enemy disarmed![/green]")
elif (spell.lower() == "alohomora" or spell == "2"):
    console.print("Door unlocked!")
elif (spell.lower() == "avada kedavra" or spell == "3"):
    console.print("Enemy reduced to sludge!")
elif (spell.lower() == "protego" or spell == "4"):
    console.print("Shield's up!")
elif (spell.lower() == "lumos" or spell == "5"):
    console.print("Light's up!")
elif (spell.lower() == "petrificus totalus" or spell == "6"):
    console.print("Enemy bound!")
else:
    quit