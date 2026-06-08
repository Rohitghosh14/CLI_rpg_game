# ⚔️ Mini RPG Battle — Terminal Edition

> *Inspired by **Genshin Impact** by HoYoverse — a love letter to Teyvat, built in Python.*

A terminal-based RPG battle game where you choose a character, explore locations from the world of Genshin Impact, and fight monsters — all from your command line.

---

## 🌍 Lore & Inspiration

This project is inspired by **Genshin Impact**, the open-world action RPG by HoYoverse.
The characters, locations, enemies, and even the currency (Primogems!) are all drawn from the game's universe.

| Game Element | In This Project |
|---|---|
| Aether, Mavuika, Mualani | Playable characters |
| Hilichurls, Hunters, Slimes | Enemy encounters |
| The Abyss | Final boss |
| Primogems | Reward currency |
| Paimon | Emergency heal item 🥲 |
| Teyvat, Natlan, Celestia | Explorable locations |

---

## 🗂️ Project Architecture

```
mini_rpg_battle/
│
├── main.py        # All game logic — characters, enemies, battle loop, map
└── README.md      # Project documentation (this file)
```

### Code Structure (Inside `main.py`)

```
main.py
│
├── 📦 Data Definitions
│   ├── classes        → Player character stats (hp, attack range)
│   ├── enemy_class    → Enemy stats (hp, attack range)
│   ├── inventory      → food, primo, paimon counts
│   └── map_location   → List of explorable areas
│
├── ⚔️  battle()        → Core fight function
│   ├── Player actions: attack / heal / paimon / run
│   ├── Monster counter-attack logic
│   ├── Primogem reward on kill
│   └── Death / game-over handling
│
└── 🔁 Main Game Loop
    ├── Character selection
    ├── Location selection
    ├── Random encounter (70% chance)
    └── Inventory display after each round
```

---

## 🎮 How to Play

```bash
# Clone the repo
git clone https://github.com/Rohitghosh14/<repo-name>.git
cd <repo-name>

# Run the game
python main.py
```

### Character Select

| Character | HP | Attack Range |
|---|---|---|
| ⚡ Aether | 200 | 45 – 105 |
| 🔥 Mavuika | 500 | 70 – 190 |
| 🌊 Mualani | 350 | 60 – 180 |

### Enemy Roster

| Enemy | HP | Attack Range |
|---|---|---|
| 🗡️ Hunter | 110 | 30 – 70 |
| 👺 Hilichurl | 80 | 25 – 50 |
| 🟢 Big Slime | 150 | 40 – 100 |
| 💀 Abyss (Boss) | 600 | 50 – 130 |

### Battle Actions

| Command | Effect |
|---|---|
| `attack` | Deal random damage from your attack range |
| `heal` | Restore 30–50 HP using food (3 uses) |
| `paimon` | Emergency heal: 100–1200 HP (1 use) 🥲 |
| `run` | Escape the battle |

### Inventory

| Item | Starting Count | Use |
|---|---|---|
| 🍖 Food | 3 | Heal 30–50 HP per use |
| 💎 Primo | 0 | Earned by defeating enemies |
| 🧚 Paimon | 1 | Emergency: heal 100–1200 HP |

> 💎 Defeat enemies to earn **Primogems (30–60 per kill)**. Collect them all, Traveler!

---

## ✨ Features

- ✅ 3 playable characters with unique stat profiles
- ✅ 4 enemy types including a final boss (The Abyss)
- ✅ Random encounter system (70% battle / 30% peaceful)
- ✅ Inventory system with limited healing resources
- ✅ Primogem reward economy
- ✅ Emergency Paimon heal (truly the last resort 🥲)
- ✅ Game-over state with lore-accurate death message
- ✅ Input validation throughout

---

## 📚 Study Notes — Python Concepts Used

### 1. Nested Dictionaries for Game Data
```python
classes = {
    "mavuika": {"hp": 500, "attack": (70, 190)}
}
```
> 💡 Each character is a dictionary *inside* a dictionary.
> This is called a **nested dict** — a very common pattern for storing
> structured data like game stats, configs, and JSON APIs.

---

### 2. `.copy()` — Why It Matters
```python
player = classes[player_select].copy()
```
> 💡 Without `.copy()`, `player` would be a **reference** to the original dict.
> Modifying `player["hp"]` would also change `classes["mavuika"]["hp"]` permanently!
> `.copy()` creates an independent shallow copy so the original stats stay intact
> for future playthroughs.

---

### 3. Tuple Unpacking with `*` in `random.randint()`
```python
dmg = random.randint(*player["attack"])
# player["attack"] = (45, 105)
# * unpacks it as: random.randint(45, 105)
```
> 💡 The `*` operator **unpacks** an iterable into positional arguments.
> This is cleaner than writing `random.randint(player["attack"][0], player["attack"][1])`.

---

### 4. `random.random()` for Probability
```python
if random.random() < 0.7:   # 70% chance of encounter
```
> 💡 `random.random()` returns a float between 0.0 and 1.0.
> Comparing it to a threshold gives you a **percentage probability** —
> a classic game dev technique for random events.

---

### 5. `random.choice()` on Dictionary Keys
```python
monster_name = random.choice(list(enemy_class.keys()))
```
> 💡 `dict.keys()` returns a view, not a list — so you must wrap it in `list()`
> before passing to `random.choice()`.

---

### 6. Passing Mutable Objects to Functions
```python
def battle(player, monster, inventory, map_location):
    inventory["food"] -= 1   # modifies the ORIGINAL dict
```
> 💡 Dictionaries are **mutable** and passed **by reference**.
> Changes inside `battle()` reflect in the original `inventory` in the main loop —
> no need to return it. This is different from integers/strings (which are immutable).

---

### 7. f-strings with Dictionary Access
```python
print(f"Your HP: {player['hp']} | Monster HP: {monster['hp']}")
```
> 💡 Inside an f-string using `"double quotes"`, use `'single quotes'`
> for dictionary keys to avoid a `SyntaxError`.

---

### 8. `quit()` for Hard Game Over
```python
if player["hp"] < 0:
    print("💀 You died!!")
    quit()
```
> 💡 `quit()` exits the entire Python program immediately.
> In a more advanced version, you'd raise a custom exception or
> return a game-over flag instead — but `quit()` is perfectly fine for terminal scripts.

---

## 🐛 Known Bugs to Fix

| Bug | Location | What's Wrong |
|---|---|---|
| `elif` indentation on `paimon` action | `battle()` | `paimon` only triggers when `heal` fails — needs its own `elif action == "paimon"` block |
| `hp < 0` death check | `battle()` | Should be `hp <= 0` — player survives at exactly 0 HP currently |
| No win condition | Main loop | Game runs forever even after defeating The Abyss boss |
| No final primo summary | End of game | Total Primogems collected aren't shown when quitting |

> 💡 Try fixing these bugs yourself — each one is a great mini-challenge!

---

## 🔮 Possible Upgrades

| Upgrade | Concept Practiced |
|---|---|
| Refactor into `Player` and `Enemy` classes | OOP, encapsulation |
| Save / load game state to `.json` | File I/O, JSON module |
| Add elemental reactions (pyro / hydro / etc.) | Dictionaries, game logic |
| Add a shop to spend Primogems | Conditionals, inventory management |
| Add a GUI with `CustomTkinter` | GUI development |
| Add character levelling and XP system | OOP, arithmetic |

---

## 👤 Author

**Rohit Ghosh** — [@Rohitghosh14](https://github.com/Rohitghosh14)

*All Genshin Impact characters, lore, and elements belong to **HoYoverse**. This is a fan-made, non-commercial learning project.*
