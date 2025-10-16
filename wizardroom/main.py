from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import random

class character():
    def __init__(self):
        self.hp = 30 # direct value
        self.maxHp = 30
        self.power = 5 # direct value
        self.damage = 5
        self.armor = 15 # direct value. If the opponent's attack class is higher than the armor class, it gets to be proccessed. Otherwise, its a [attack] out of [defense] chance to be processed.

    def attack(self, opponent):
        if (random.randint(0, self.armor) <= opponent.power):
            self.hp = self.hp - opponent.damage
            return True
        else:
            return False
        
    def heal(self):
        self.hp = self.maxHp
        
class goblin(character):
    def __init__(self):
        super().__init__()

class player(character):
    def __init__(self):
        super().__init__()
        self.hp = 80
        self.maxHp = 80
        self.power = 12
        self.damage = 10
        self.armor = 20


console = Console()
currentRoomSymbol = "▮"
roomSymbol = "▯"
rooms = {
    "room1": {
        "name": "Entrance",
        "links": {
            "north": "room2"
        },
        "position": [0,0],
        "desc": "You stand before a dimly-lit doorway entrance to a massive castle. Goblins can be seen patrolling on top of the walls, and a few cast glaces down upon you. Your kind may not be very welcome here...",
        "tooltip": "Go back to whence you came...",
        "enemies": {}
    },
    "room2": {
        "name": "Hallway",
        "links": {
            "north": "room3",
            "south": "room1"
        },
        "position": [0,1],
        "desc": "You now stand inside the hallway towards the castle... You have a feeling that, after this point, there is no turning back. Are you sure about this?",
        "tooltip": "Proceed into the castle...",
        "enemies": {}
    },
    "room3": {
        "name": "Hallway",
        "links": {
            "east": "room4",
            "west": "room5"
        },
        "position": [0,2],
        "desc": "3 hooting goblins notice you! Prepare for a fight!",
        "tooltip": "I'm ready.",
        "enemies": {
            "gob1": goblin(),
            "gob2": goblin(),
            "gob3": goblin()
        }
    },
}

def printRoomDesc(room):
    console.print(f"[blue]{rooms[room]["desc"]}[/blue]")

printRoomDesc("room1")