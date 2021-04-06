import random

#asking the user for an input
users_Choice = int(input ('''What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n''' ))


#this line of code is very important because it (else we will be have a kind of issue whereby the computer choice will be printing)
#check if it is greater than the intended range of value i.e. (not > 2)
#else it continue running it program as usual
if users_Choice >= 3 or users_Choice < 0:
     print ("You Inserted the Wrong Input")
     print("Please Input a Number in range of 0 to 2")
else:
    
    # using conditional to decide where Rock Paper and Scissor should be placed
    if users_Choice == 0:
        print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''')
    elif users_Choice== 1:
        print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        ''')
    elif users_Choice== 2:
        print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        ''')

        
    #computer Part of the game    
    print ("Computer Choose:")

    #computer choosing at random
    computerChoice = int(random.choice(["0", "1", "2"]))

    if computerChoice == 0:
        print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''')
    elif computerChoice == 1:
        print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
        ''')
    elif computerChoice == 2:
        print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        ''')

                    #GAME CONDITION
    # Draw Condition
    if users_Choice == computerChoice:
        print ("DRAW")
        
    #Rock wins against scissors condition
    elif users_Choice == 0 and computerChoice == 2:
        print ("⚡⚡⚡ YOU WIN!!! ⚡⚡⚡")
        print ("✨✨✨ CONGRATULATION ✨✨✨")
    elif users_Choice == 2 and computerChoice == 0:
        print ("🛡🛡🛡 COMPUTER WIN 🛡🛡🛡")
        print ("PLEASE TRY AGAIN")
        
    #Scissors win against paper condition
    elif users_Choice == 2 and computerChoice == 1:
        print ("⚡⚡⚡ YOU WIN!!! ⚡⚡⚡")
        print ("✨✨✨ CONGRATULATION ✨✨✨")
    elif users_Choice == 1 and computerChoice == 2:
        print ("🛡🛡🛡 COMPUTER WIN 🛡🛡🛡")
        print ("PLEASE TRY AGAIN")
        
    #Paper wins against rock condition
    elif users_Choice == 1 and computerChoice == 0:
        print ("⚡⚡⚡ YOU WIN!!! ⚡⚡⚡")
        print ("✨✨✨ CONGRATULATION ✨✨✨")
    elif users_Choice == 0 and computerChoice == 1:
        print ("🛡🛡🛡 COMPUTER WIN 🛡🛡🛡")
        print ("PLEASE TRY AGAIN")


