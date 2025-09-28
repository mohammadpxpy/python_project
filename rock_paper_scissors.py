#mhmhpx سنگ کاغذ قیچی
import random

def game():
    win = 0
    lose = 0
    while True:
        list_choice = ["rock","paper","scissors"]
        choise_system = random.choice(list_choice)

        user = input("  << exit >>  << rock paper scissors >> \n ENTER: ")

        if choise_system == user:
                print("Equal😬, try again")
        elif choise_system ==  "rock" and user == "paper":
            print("win!🤩")
            win += 1
        elif choise_system == "paper" and user == "scissors":
            print("win!🤩")
            win += 1
        elif choise_system == "scissors" and user == "rock":
            print("win!🤩")
            win += 1  
        elif user == "exit":
            print("come again🙃")
        elif user not in list_choice :
            print("plase true choice : rock paper scissors ")
            continue
        else:
            print("lose😓")
            lose += 1
        
        print(f"win : {win}")
        print(f"lose : {lose}")
game()
    