# Legendary Tribble

A console-based cross between a MUD and a roguelike. Descend stairs, fight monsters, grab loot, and capture the `legendary tribble` from the bottom of the dungeon. Procedural generation guarantees each foray back into the dungeon provides a different experience.

To play, run `python play.py`. Built and tested with Python 2.7

# Short Sample Play Session

```
Welcome to Legendary Tribble!

Instructions: type 'fight <name>' to fight a monster.
Kill all the monsters, then, type 'descend' to go to the next floor
If you want to go back up one floor, type 'ascend'.

You are on floor B1.

You see 5 monsters:
Health: 50/50
A rat
A goblin
A ogre
A goblin
A ogre
> fight goblin
You attack the goblin!
Player: 50/50 goblin: 20/20
You attacks goblin for 6 damage!
Player: 50/50 goblin: 14/20
You attacks goblin for 6 damage!
goblin attacks You for 3 damage!
Player: 47/50 goblin: 8/20
You attacks goblin for 6 damage!
Player: 47/50 goblin: 2/20
You attacks goblin for 6 damage!
goblin attacks You for 3 damage!
Victory! You vanquished your foe!
You see 4 monsters:
Health: 44/50
A rat
A ogre
A goblin
A ogre
> fight rat
You attack the rat!
Player: 44/50 rat: 10/10
You attacks rat for 6 damage!
rat attacks You for 1 damage!
Player: 43/50 rat: 4/10
You attacks rat for 6 damage!
rat attacks You for 1 damage!
Victory! You vanquished your foe!
You see 3 monsters:
Health: 42/50
A ogre
A goblin
A ogre
> quit
Bye!
```