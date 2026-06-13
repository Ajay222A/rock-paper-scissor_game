import random

list1=["Rock", "Paper", "Scissors"]

while True:

    print("choice only one option")
    print(f"1. {list1[0]}\n2. {list1[1]}\n3. {list1[2]}\n4. Exit\n")
    choice=input()
    if choice == '4':
        break
    elif choice == '1' or choice == '2' or choice == '3':

        if choice=="1":
            choice="Rock"
            print(f"You chose {list1[0]}")
        elif choice=="2":
            choice="Paper"
            print(f"You chose {list1[1]}")
        elif choice=="3":
            choice="Scissors"
            print(f"You chose {list1[2]}")

        computer_choice=random.choice(list1)
        print(f"Computer chose {computer_choice}")
        if computer_choice==choice:
            print(f"It's a Draw!")
        elif computer_choice=="Rock" and choice=="Scissors":
            print("you Lose")
        elif computer_choice=="Rock" and choice=="Paper":
            print("you Win")
        elif computer_choice=="Paper" and choice=="Rock":
            print("you Lose")
        elif computer_choice=="Paper" and choice=="Scissors":
            print("you Win")
        elif computer_choice=="Scissors" and choice=="Rock":
            print("you Win")
        elif computer_choice=="Scissors" and choice=="Paper":
            print("you Lose")
    else:
        print("Oops, invalid choice!Try again")
        print(choice)