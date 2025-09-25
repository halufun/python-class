from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import random


console = Console()

startNumber = 1 + random.randint(0, 20)
endNumber = 1 + startNumber + random.randint(0, 100)
myNumber = random.randint(startNumber, endNumber)

console.print("My terminal has a custom theme, which does not support all ansi escape sequences. Yellow, Green: Does not display correct.")
console.print(f"[bold green]I have a number between [bold red]{startNumber}[/bold red] and [bold red]{endNumber}[/bold red], guess what it is![/bold green]")

while True:
    guess = Prompt.ask("[red]Make a guess[/red]")
    if guess == "quit":
        break
    try:
        guess = int(guess)
    except ValueError:
        console.print(f"[bold red]Error! - Invalid input![/bold red]")
        # quit()
        continue

    console.print(f"[yellow]You guessed: {guess}[/yellow]")

    if guess == myNumber:
        console.print("[green]You guessed it![/green]")
        break
    else:
        console.print("[red]Wrong![/red]")

console.print("[green]Thanks for playing![/green]")