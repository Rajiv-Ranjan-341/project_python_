name = input("Type your name: ")
print("Welcome", name, "to this adventure!")


def get_input(prompt, options):
    while True:
        answer = input(prompt).lower()
        if answer in options:
            return answer
        else:
            print("Not a valid option. Please try again.")

answer1 = get_input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ",
    ["left", "right"])

if answer1 == "left":
    answer2 = get_input(
        "You come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ",
        ["walk", "swim"])

    if answer2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer2 == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")

elif answer1 == "right":
    answer3 = get_input(
        "You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ",
        ["cross", "back"])

    if answer3 == "back":
        print("You go back and lose.")
    elif answer3 == "cross":
        answer4 = get_input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ",
            ["yes", "no"])

        if answer4 == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer4 == "no":
            print("You ignore the stranger and they are offended and you lose.")

print("Thank you for trying", name)
