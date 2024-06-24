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

# Write your code below this line 👇

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if choose >= 3 or choose < 0:
    print("You typed an invalid number, you lose!")
elif choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

RPS_computer = random.randint(0, 2)

if choose >= 3 or choose < 0:
    print("-")
else:

    print("Computer chose:\n")

if RPS_computer == 0:
    print(rock)
    if choose == 2:
        print("You lose")
    elif choose == 1:
        print("You win")
    elif choose == 0:
        print("Tie")


elif RPS_computer == 1:
    print(paper)
    if choose == 2:
        print("You win")
    elif choose == 1:
        print("Tie")
    elif choose == 0:
        print("You lose")

elif RPS_computer == 2:
    print(scissors)
    if choose == 2:
        print("Tie")
    elif choose == 1:
        print("You lose")
    elif choose == 0:
        print("You win")





