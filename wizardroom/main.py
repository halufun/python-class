from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import random
import json
import os

file_path = os.path.abspath(__file__)
save_path = f"{os.path.dirname(file_path)}\\saves\\1.save"
try:
    with open(save_path, "x") as temp:
        temp.write("")
except:
    pass
class data():
    def save(savedata):
        f = None
        with open(save_path, "w") as f:
            f.write(str(savedata))
    def load():
        f = open(save_path)
        return str(f)
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
class orc(character):
    def __init__(self):
        super().__init__()
        self.hp = 120
        self.armor = 50
        self.power = 20
        self.maxHp = 120
        self.damage = 15
class skeleton(character):
    def __init__(self):
        super().__init__()
        self.hp = 15
        self.armor = 5
        self.power = 10
        self.maxHp = 15
        self.damage = 30

class player(character):
    def __init__(self):
        super().__init__()
        self.hp = 80
        self.maxHp = 80
        self.power = 12
        self.damage = 10
        self.armor = 20

currentRoomSymbol = "▮"
roomSymbol = "▯"
console = Console()
vars = {
    "playerchar": player(),
    "currentRoom": "room1",

    "characters": {
        "sneed": goblin(),
        "bingus": goblin(),
        "wurgus": orc(),
        "snorblot": goblin(),
        "skattle": skeleton()
    },

    "rooms": {
        "room1": {
            "name": "Entrance",
            "links": {
                "north": "room2"
            },
            "position": [0,0],
            "desc": "You stand before a dimly-lit doorway entrance to a massive castle. Goblins can be seen patrolling on top of the walls, and a few cast glaces down upon you. Your kind may not be very welcome here...",
            "tooltip": "Go back to whence you came...",
            "cleared": True,
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
            "cleared": True,
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
            "cleared": False,
            "enemies": {
                "gob1": goblin(),
                "gob2": goblin(),
                "gob3": goblin()
            }
        }
    }
}

def printRoomDesc(room):
    console.print(f"[blue]{vars["rooms"][room]["desc"]}[/blue]")
data.save(vars)

printRoomDesc("room1")
console.print(f"The available rooms are:\n{vars["rooms"]["room1"]["links"]}")
vars["playerchar"].hp = 15
console.print(f"Your health is currently: {vars["playerchar"].hp}\n")
console.print("Choose an option:")
console.print("1 - Heal")
console.print("2 - Move rooms")

answer = Prompt.ask("Pick a number")

match answer:
    case "1":
        vars["playerchar"].heal()
    case "2":
        pass
console.print(f"Your health is currently: {vars["playerchar"].hp}\n")
data.load()
console.print(vars)
console.print(f"Your health is currently: {vars["playerchar"].hp}\n")