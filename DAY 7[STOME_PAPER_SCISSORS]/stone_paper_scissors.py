import random

print("------ Stone Paper Scissors Game ------\n")

# options list for computer
options = ["stone", "paper", "scissors"]

# mapping numbers to signs
signs = {
    1: "stone",
    2: "paper",
    3: "scissors"
}
print("Choose your move:")
print("1 = stone")
print("2 = paper")
print("3 = scissors\n")

# taking input
your_choice = int(input("Enter your choice (1/2/3): "))

# checking wrong input
if your_choice not in signs:
    print("\nWrong input bro! Please enter only 1, 2 or 3.")

else:
    your_sign = signs[your_choice]
    computer_sign = random.choice(options)

    print("\nYou chose:", your_sign)
    print("Computer chose:", computer_sign)
    print("--------------------------------------")

    # draw
    if your_sign == computer_sign:
        print("Result: It's a Draw!")

    # all winning cases
    elif your_sign == "stone" and computer_sign == "scissors":
        print("Result: You Win! Stone breaks Scissors")
    elif your_sign == "paper" and computer_sign == "stone":
        print("Result: You Win! Paper covers Stone")
    elif your_sign == "scissors" and computer_sign == "paper":
        print("Result: You Win! Scissors cuts Paper")

    # all losing cases
    elif your_sign == "stone" and computer_sign == "paper":
        print("Result: You Lose! Paper covers Stone")
    elif your_sign == "paper" and computer_sign == "scissors":
        print("Result: You Lose! Scissors cuts Paper")
    elif your_sign == "scissors" and computer_sign == "stone":
        print("Result: You Lose! Stone breaks Scissors")
    else:
        print("error!")