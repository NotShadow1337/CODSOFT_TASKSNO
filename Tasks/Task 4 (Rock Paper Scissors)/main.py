import random

while True:
    print("\n----- ROCK PAPER SCISSORS -----")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you!")
        break

    if choice == "1":
        user = "Rock"
    elif choice == "2":
        user = "Paper"
    elif choice == "3":
        user = "Scissors"
    else:
        print("Invalid choice.")
        continue

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You win!")

    else:
        print("Computer wins!")