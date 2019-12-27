#define the choices
options = ["rock", "paper", "scissors"]

#player 1 input
p1choice = (input("Player 1 please choose rock, paper or scissors: "))
if p1choice not in options:
    print("Sorry you can only enter rock, paper, or scissors")

#player 2 input
p2choice = (input("Player 2 please choose rock, paper or scissors: "))
if p2choice not in options:
    print("Sorry you can only enter rock, paper, or scissors")

#tie
if p1choice == p2choice:
    print("Tie try again")

#player 1 wins
if p1choice == ("rock") and p2choice == ("scissors"):
    print("Rocks Smashes Scissors Player 1 Wins")
elif p1choice ==("paper") and p2choice == ("rock"):
    print("Paper Covers Rock Player 1 Wins")
elif p1choice ==("scissors") and p2choice == ("paper"):
    print("Scissors Cut Papaer Player 1 Wins")

#player2 wins
elif p2choice == ("rock") and p1choice == ("scissors"):
    print("Rocks Smashes Scissors Player 2 Wins")
elif p2choice ==("paper") and p1choice == ("rock"):
    print("Paper Covers Rock Player 2 Wins")
elif p2choice ==("scissors") and p1choice == ("paper"):
    print("Scissors Cut Papaer Player 2 Wins") 

print (p1choice, p2choice)