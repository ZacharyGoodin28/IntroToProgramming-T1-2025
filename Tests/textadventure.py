inventory = []
has_crystal = False


def start_game():
    print("Welcome, adventurer, to the Quest for the Lost Crystal!")
    print("You stand at a crossroads near a mysterious forest.")
    print("1. Enter the forest.")
    print("2. Head toward the mountains.")
    print("3. Visit the nearby village.")

    choice = input("> ")
    if choice == "1":
        forest_entrance()
    elif choice == "2":
        mountain_path()
    elif choice == "3":
        village_square()
    else:
        print("Invalid choice. Try again.")
        start_game()

def forest_entrance():
    print("\nYou step into the dark forest. The trees whisper your name.")
    print("1. Follow a strange glowing light.")
    print("2. Climb a tall tree to get your bearings.")
    print("3. Go back to the crossroads.")

    choice = input("> ")
    if choice == "1":
        glowing_light()
    elif choice == "2":
        climb_tree()
    elif choice == "3":
        start_game()
    else:
        print("Invalid choice. Try again.")
        forest_entrance()

def glowing_light():
    print("\nYou approach the light and find a fairy trapped in a jar.")
    print("1. Free the fairy.")
    print("2. Ignore it and keep walking.")

    choice = input("> ")
    if choice == "1":
        print("The fairy thanks you and gives you a magic amulet!")
        inventory.append("amulet")
        fairy_reward()
    elif choice == "2":
        wolf_attack()
    else:
        print("Invalid choice. Try again.")
        glowing_light()

def climb_tree():
    print("\nFrom the top, you spot smoke rising in the east and a river in the west.")
    print("1. Head toward the smoke.")
    print("2. Follow the river.")
    choice = input("> ")
    if choice == "1":
        bandit_camp()
    elif choice == "2":
        river_bank()
    else:
        print("Invalid choice. Try again.")
        climb_tree()

def fairy_reward():
    print("\nThe fairy disappears into the mist. You feel protected.")
    print("1. Continue deeper into the forest.")
    print("2. Rest under a tree.")
    choice = input("> ")
    if choice == "1":
        forest_clearing()
    elif choice == "2":
        deep_sleep()
    else:
        print("Invalid choice. Try again.")
        fairy_reward()


def wolf_attack():
    print("\nA wolf leaps from the shadows!")
    if "amulet" in inventory:
        print("Your amulet glows and scares the wolf away!")
        forest_clearing()
    else:
        print("The wolf overpowers you...")
        ending_death()

def forest_clearing():
    print("\nYou find an ancient stone door covered in runes.")
    print("1. Try to open the door.")
    print("2. Search around the clearing.")
    choice = input("> ")
    if choice == "1":
        stone_door()
    elif choice == "2":
        hidden_scroll()
    else:
        print("Invalid choice. Try again.")
        forest_clearing()


def stone_door():
    print("\nThe runes glow faintly. You need a magic key to open it.")
    if "key" in inventory:
        secret_chamber()
    else:
        print("You can't open it yet.")
        forest_clearing()

def hidden_scroll():
    print("\nYou find a scroll revealing the door needs a 'key of light'.")
    print("1. Go search for the key.")
    print("2. Ignore the scroll and leave.")
    choice = input("> ")
    if choice == "1":
        river_bank()
    elif choice == "2":
        forest_exit()
    else:
        print("Invalid choice. Try again.")
        hidden_scroll()

def river_bank():
    print("\nYou reach a calm river.")
    print("1. Swim across.")
    print("2. Build a raft.")
    choice = input("> ")
    if choice == "1":
        print("The current pulls you under...")
        ending_drown()
    elif choice == "2":
        print("You safely cross and find a glowing key!")
        inventory.append("key")
        stone_door()
    else:
        print("Invalid choice. Try again.")
        river_bank()

def secret_chamber():
    global has_crystal
    print("\nThe door opens to reveal the Lost Crystal on a pedestal!")
    print("1. Take the crystal.")
    print("2. Leave it alone.")
    choice = input("> ")
    if choice == "1":
        print("You take the crystal — it pulses with power.")
        has_crystal = True
        escape_tunnel()
    elif choice == "2":
        forest_exit()
    else:
        print("Invalid choice. Try again.")
        secret_chamber()

def escape_tunnel():
    print("\nA secret tunnel leads out of the forest.")
    print("1. Go through it.")
    print("2. Stay behind to explore more.")
    choice = input("> ")
    if choice == "1":
        ending_escape()
    elif choice == "2":
        bandit_camp()
    else:
        print("Invalid choice. Try again.")
        escape_tunnel()

def deep_sleep():
    print("\nYou fall asleep and wake up surrounded by vines!")
    print("1. Try to break free.")
    print("2. Call for help.")
    choice = input("> ")
    if choice == "1":
        print("You break free and escape to the clearing.")
        forest_clearing()
    elif choice == "2":
        print("No one comes. The vines tighten...")
        ending_death()
    else:
        print("Invalid choice. Try again.")
        deep_sleep()

def mountain_path():
    print("\nYou climb the rocky trail of the mountains.")
    print("1. Enter a cave.")
    print("2. Keep climbing.")
    choice = input("> ")
    if choice == "1":
        mountain_cave()
    elif choice == "2":
        mountain_peak()
    else:
        print("Invalid choice. Try again.")
        mountain_path()

def mountain_cave():
    print("\nYou find an old chest inside the cave.")
    print("1. Open the chest.")
    print("2. Leave it alone.")
    choice = input("> ")
    if choice == "1":
        print("You find a map leading to the crystal’s location!")
        inventory.append("map")
        forest_entrance()
    elif choice == "2":
        mountain_peak()
    else:
        print("Invalid choice. Try again.")
        mountain_cave()

def mountain_peak():
    print("\nAt the peak, you see the entire land below.")
    print("A storm brews — you must decide quickly.")
    print("1. Build shelter.")
    print("2. Climb down.")
    choice = input("> ")
    if choice == "1":
        print("Lightning strikes the peak...")
        ending_death()
    elif choice == "2":
        forest_exit()
    else:
        print("Invalid choice. Try again.")
        mountain_peak()


def bandit_camp():
    print("\nYou stumble upon a camp of bandits!")
    print("1. Sneak past them.")
    print("2. Confront them.")
    choice = input("> ")
    if choice == "1":
        forest_exit()
    elif choice == "2":
        print("They overpower you...")
        ending_death()
    else:
        print("Invalid choice. Try again.")
        bandit_camp()


def forest_exit():
    print("\nYou find your way out of the forest.")
    if has_crystal:
        ending_victory()
    else:
        ending_empty_handed()

def village_square():
    print("\nYou arrive at a peaceful village.")
    print("1. Visit the inn.")
    print("2. Talk to the blacksmith.")
    choice = input("> ")
    if choice == "1":
        village_inn()
    elif choice == "2":
        village_blacksmith()
    else:
        print("Invalid choice. Try again.")
        village_square()

def village_inn():
    print("\nThe innkeeper tells tales of a hidden crystal in the forest.")
    print("1. Set out for the forest.")
    print("2. Stay and rest.")
    choice = input("> ")
    if choice == "1":
        forest_entrance()
    elif choice == "2":
        print("You live a quiet life as a storyteller.")
        ending_peaceful()
    else:
        print("Invalid choice. Try again.")
        village_inn()

def village_blacksmith():
    print("\nThe blacksmith offers to forge you a sword.")
    print("1. Accept and wait.")
    print("2. Decline and leave.")
    choice = input("> ")
    if choice == "1":
        print("You gain a sword of courage!")
        inventory.append("sword")
        forest_entrance()
    elif choice == "2":
        start_game()
    else:
        print("Invalid choice. Try again.")
        village_blacksmith()




def ending_victory():
    print("\n You return home with the Lost Crystal! The kingdom celebrates your bravery!")
    print("=== ENDING 1: Hero of the Realm ===")

def ending_empty_handed():
    print("\nYou leave the forest without the crystal, but with a story to tell.")
    print("=== ENDING 2: The Wanderer ===")

def ending_death():
    print("\n You met your untimely end.")
    print("=== ENDING 3: Tragic Fate ===")

def ending_peaceful():
    print("\nYou settle down in the village, living peacefully for the rest of your days.")
    print("=== ENDING 4: The Peaceful Life ===")

def ending_drown():
    print("\n The river claims your life.")
    print("=== ENDING 5: The Depths ===")

def ending_escape():
    print("\n You escape the forest safely, crystal in hand, ready for new adventures.")
    print("=== ALTERNATE VICTORY ENDING ===")


if __name__ == "__main__":
    start_game()


