
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def random_event():
    events = [
        "You encounter a friendly squirrel who leads you to a shortcut. You move forward with ease!",
        "You find a hidden treasure chest! You open it and gain extra supplies.",
        "A sudden storm appears! You take shelter and wait for it to pass.",
        "You stumble upon a magical portal! Do you dare to enter it? (yes/no): "
    ]
    event = random.choice(events)
    if event == "You stumble upon a magical portal! Do you dare to enter it? (yes/no): ":
        answer = get_input(event, ["yes", "no"])
        if answer == "yes":
            print("You enter the portal and find yourself in a parallel universe. You WIN!")
        else:
            print("You decide not to enter the portal and continue on your journey.")
    else:
        print(event)

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
        print("You walked for many miles, ran out of water, and you lost.")

elif answer1 == "right":
    answer3 = get_input(
        "You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ",
        ["cross", "back"])

    if answer3 == "back":
        print("You go back and lose.")
    elif answer3 == "cross":
        random_event()  # Introduce a random event after crossing the bridge

print("Thank you for trying", name)
