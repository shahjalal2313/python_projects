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

choice_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
    print("you put an invalid number. Please choose a number between 0 t0 2")
else:
    print(f"You choose: {user_choice}")
    print(choice_list[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"computer_chosen: {computer_choice}")
    print(choice_list[computer_choice])

    if user_choice==0 and computer_choice==2:
        print("You Win!")
    elif user_choice==2 and computer_choice==0:
        print("you loose!")
    elif user_choice > computer_choice:
        print("You Win")
    elif user_choice < computer_choice:
        print("You Loose!")
    else:
        print("Draw!")