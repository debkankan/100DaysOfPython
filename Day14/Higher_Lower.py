import art
from game_data import data
import random

print(art.logo)

game_on = True
score = 0

def higher_lower():
    global score
    global game_on
    a = random.choice(data)
    b = random.choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}\n")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}\n")
    choice = input("Who has more followers? Type 'A' or 'B':\t").upper()
    if (choice == 'A'):
        if (a['follower_count'] > b['follower_count']):
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry that was wrong. Final Score: {score}")
            game_on = False
    else:
        if (a['follower_count'] < b['follower_count']):
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry that was wrong. Final Score: {score}")
            game_on = False


while game_on:
    higher_lower()



