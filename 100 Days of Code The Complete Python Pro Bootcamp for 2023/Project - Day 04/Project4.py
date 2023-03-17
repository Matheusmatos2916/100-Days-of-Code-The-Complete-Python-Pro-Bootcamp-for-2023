# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

stage = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if stage >= 3 or stage < 0:
     print("You typed an invalid number, you lose!")
else:
    game_images = [rock, paper, scissors]
    pc = random.randint(0, 2)

print(f"Your chose: {stage}")
print(game_images[stage])
    
print(f"Computer chose: {pc}")
print(game_images[pc])

if stage == 0 and pc == 2:
     print("You wins!")
elif pc == 0 and stage == 2:
     print("You lose!")
elif pc > stage:
    print("You lose!")
elif stage > pc:
    print("You wins!")
elif pc == stage:
    print("it's draw")

