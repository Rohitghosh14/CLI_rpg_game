import random

print("⚔️  WELCOME TO MINI RPG BATTLE ⚔️")

classes = { 
            "aether":{"hp":200,"attack":(45,105)},
            "mavuika":{"hp":500,"attack":(70,190)},
            "mualani":{"hp":350,"attack":(60,180)}
            
}
enemy_class = {
            "hunter":{"hp":110,"attack":(30,70)},
            "hilicher":{"hp":80,"attack":(25,50)},
            "big-slimes":{"hp":150,"attack":(40,100)},
            "Abyss💀(boss)":{"hp":600,"attack":(50,130)}
}
inventory = {
            "food" : 3,
            "primo" : 0,
            "paimon" : 1
}
map_location = ["tevyat","celestia","moon","natlan"]

def battle(player,monster,inventory,map_location):

    print(f"\n⚔️ A wild {monster['name']} appeared!")

    while monster["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour Hp:{player["hp"]} | Monster Hp:{monster["hp"]}")
        action = input("Enter your Move[Attack/Heal/Run/paimon]: ").lower()

        if action == "attack":
            dmg = random.randint(*player["attack"])
            monster["hp"] -= dmg
            print(f"You dealt {dmg} damage!")

        elif action == "heal":
            if inventory["food"] > 0:
                heal = random.randint(30,50)
                player["hp"]+=heal
                inventory["food"]-=1
        elif inventory["paimon"] > 0:
            heal = random.randint(100,1200)
            player["hp"] += heal
            inventory["paimon"] -= 1
            print("Emergency food used!!! 🥲")
            print(f"You healed {heal} HP!")
        elif action == "run":
            print(f"you escaped!!")
            return
        else:
            print("Invalid action")
            continue

        if monster["hp"] <= 0:
            primo = random.randint(30,60)
            inventory["primo"] += primo
            print(f"\n🏆 You defeated the {monster['name']}!")
            print(f"\n you found primogems: {primo}")
            break

        monster_dmg = random.randint(*monster["attack"])
        player["hp"]-=monster_dmg
        print(f"\n {monster["name"]} attack you!!")
        print(f"you get {monster_dmg} damage!!! \n be-carefull!!")

        if player["hp"]<0:
            print(f"💀 {player["name"]} you died!! ")
            print(f"{map_location} lost!! & The abyss has taken the world... 💀!!")
            quit()

    
print("⚔️ WELCOME TO TERMINAL Genshin RPG ⚔️")

print("choice your charector!!")
for c in classes:
    print("->",c)

while True:
    player_select = input("> ").lower()

    if player_select in classes:
        player = classes[player_select].copy()
        player["name"] = player_select
        print(f"\nYou chose {player_select}!")
        break
    else:
        print("please enter a valid option!!")


#main game:
while True:
    print(f"where do you want to go travelr ? {player_select} ")
    for l in map_location:
        print("->",l)

    map_select = input("Enter where you want to teleport!! ").lower()
    if map_select not in map_location:
        print("we can't teleport there!!")
        continue

    print(f"\nYou travel to the {map_select}...")

    if random.random() < 0.7:
        monster_name = random.choice(list(enemy_class.keys()))
        monster = enemy_class[monster_name].copy()
        monster["name"] = monster_name
        battle(player,monster,inventory,map_select)
    else:
        print("The area is peaceful.")

    print(f"inventory: ",inventory)




