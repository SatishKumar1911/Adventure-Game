import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious forest with no memory of how you got there.")
    print("You see four paths leading in different directions.")
    print("Do you want to go 'north', 'south', 'east', or 'west'?")
    choice = input("Enter a direction: ").lower()
    clear_screen()
    if choice in ["north", "south", "east", "west"]:
        next_location(choice)
    else:
        print("Invalid choice. Please try again.")
        start_game()

def next_location(direction):
    if direction == "north":
        print("You head north and encounter a river.")
        print("Do you want to 'swim' across or 'look' for a bridge?")
        choice = input("Enter 'swim' or 'look': ").lower()
        clear_screen()
        if choice == "swim":
            print("You swim across and find a hidden cave.")
            explore_cave()
        elif choice == "look":
            print("You find a bridge and cross it.")
            print("You see a castle in the distance.")
            approach_castle()
        else:
            print("Invalid choice. Please try again.")
            next_location("north")
    elif direction == "south":
        print("You head south and find a village.")
        explore_village()
    elif direction == "east":
        print("You head east and come across a dense forest.")
        print("Do you want to 'explore' the forest or 'bypass' it?")
        choice = input("Enter 'explore' or 'bypass': ").lower()
        clear_screen()
        if choice == "explore":
            print("You find a hidden path that leads to a mystical garden.")
            explore_garden()
        elif choice == "bypass":
            print("You bypass the forest and reach a mountain range.")
            climb_mountains()
        else:
            print("Invalid choice. Please try again.")
            next_location("east")
    elif direction == "west":
        print("You head west and encounter a desert.")
        traverse_desert()

def explore_cave():
    print("You explore the cave and find a treasure chest.")
    print("Do you want to 'open' it or 'leave' it?")
    choice = input("Enter 'open' or 'leave': ").lower()
    clear_screen()
    if choice == "open":
        print("You open the chest and find a magical amulet. You win!")
    elif choice == "leave":
        print("You leave the chest behind and continue exploring the cave.")
        print("You find a secret passage that leads you out of the cave.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        explore_cave()

def approach_castle():
    print("You approach the castle and are greeted by the king.")
    print("He tells you about a dragon that is terrorizing the kingdom.")
    print("Do you want to 'fight' the dragon or 'negotiate' with it?")
    choice = input("Enter 'fight' or 'negotiate': ").lower()
    clear_screen()
    if choice == "fight":
        print("You gear up for battle and defeat the dragon. The king rewards you with a bag of gold. You win!")
    elif choice == "negotiate":
        print("You try to negotiate with the dragon, but it doesn't work. You have to flee. Game over!")
    else:
        print("Invalid choice. Please try again.")
        approach_castle()

def explore_village():
    print("You explore the village and meet the villagers.")
    print("They tell you about a nearby enchanted forest.")
    print("Do you want to 'explore' the forest or 'return' to the crossroads?")
    choice = input("Enter 'explore' or 'return': ").lower()
    clear_screen()
    if choice == "explore":
        print("You explore the forest and find a magical portal.")
        enter_portal()
    elif choice == "return":
        start_game()
    else:
        print("Invalid choice. Please try again.")
        explore_village()

def explore_garden():
    print("You explore the mystical garden and find a magical fountain.")
    print("Do you want to 'drink' from the fountain or 'move on'?")
    choice = input("Enter 'drink' or 'move on': ").lower()
    clear_screen()
    if choice == "drink":
        print("You drink from the fountain and gain eternal youth. You win!")
    elif choice == "move on":
        print("You move on from the garden and continue your journey.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        explore_garden()

def climb_mountains():
    print("You climb the mountains and reach a hidden valley.")
    print("Do you want to 'explore' the valley or 'settle' there?")
    choice = input("Enter 'explore' or 'settle': ").lower()
    clear_screen()
    if choice == "explore":
        print("You explore the valley and find a tribe of friendly nomads.")
    elif choice == "settle":
        print("You decide to settle in the valley and live a peaceful life. You win!")
    else:
        print("Invalid choice. Please try again.")
        climb_mountains()

def traverse_desert():
    print("You traverse the desert and find an oasis.")
    print("Do you want to 'rest' at the oasis or 'continue' your journey?")
    choice = input("Enter 'rest' or 'continue': ").lower()
    clear_screen()
    if choice == "rest":
        print("You rest at the oasis and regain your strength. You win!")
    elif choice == "continue":
        print("You continue your journey through the desert.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        traverse_desert()

def enter_portal():
    print("You enter the magical portal and are transported to a different realm.")
    print("Do you want to 'explore' the realm or 'return' through the portal?")
    choice = input("Enter 'explore' or 'return': ").lower()
    clear_screen()
    if choice == "explore":
        print("You explore the realm and find a powerful wizard.")
        seek_wizard()
    elif choice == "return":
        print("You return through the portal and find yourself back at the crossroads.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        enter_portal()

def seek_wizard():
    print("You seek the wizard's help to return home.")
    print("He agrees to help you but asks for a rare ingredient.")
    print("Do you want to 'find' the ingredient or 'decline' his offer?")
    choice = input("Enter 'find' or 'decline': ").lower()
    clear_screen()
    if choice == "find":
        print("You find the ingredient and return to the wizard.")
        print("He performs the spell and sends you back home. You win!")
    elif choice == "decline":
        print("You decline the wizard's offer and continue exploring the realm.")
        print("You find a portal that leads you back home. You win!")
    
start_game()