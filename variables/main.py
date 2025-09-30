from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()
age = int(Prompt.ask("[blue]How old are you?[/blue]"))
name = Prompt.ask("[blue]What is your name?[/blue]")
height = Prompt.ask("[blue]How tall are you?[/blue]")
ssn = Prompt.ask("[blue]What's your SSN?[/blue]")
# 5 more
hobby = Prompt.ask("[blue]Do you have a hobby? If so, what is it?[/blue]")
book = Prompt.ask("[blue]What is your favorite book?[/blue]")
musicArtist = Prompt.ask("[blue]Who's your favorite music artist?[/blue]")
videoGame = Prompt.ask("[blue]What's your favorite videogame?[/blue]")
favColor = Prompt.ask("[blue]What is your favorite [red]c[/red][yellow]o[/yellow][green]l[/green][blue]o[/blue][purple]r[/purple]?[/blue]")

console.print(f"[{favColor}]Hi [yellow]{name}[/yellow], you are {age} years old.[/{favColor}]")

if age < 18:
    console.print(f"[{favColor}]You are a [blue]minor[/blue].[/{favColor}]")
else:
    console.print(f"[{favColor}]You are an [blue]adult[/blue].[/{favColor}]")

console.print(f"[{favColor}]Your height is {height}.[/{favColor}]")

console.print(f"[{favColor}]Your SSN is {ssn}.[/{favColor}]")

if hobby == "no":
    console.print(f"[{favColor}]You are boring![/{favColor}]")
else:
    console.print(f"[{favColor}]Your hobby is {hobby}.[/{favColor}]")

console.print(f"[{favColor}]Your favorite book is {book}.[/{favColor}]")

console.print(f"[{favColor}]Your favorite music artist is {musicArtist}.[/{favColor}]")

console.print(f"[{favColor}]Your favorite video game is {videoGame}.[/{favColor}]")

console.print(f"[bold {favColor}]Your favorite color is {favColor}![/bold {favColor}]")