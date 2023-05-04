
#
def user_choice(question):

    # valid inputs:
    paper = ["paper", "p"]
    rock = ["rock", "r"]
    scissors = ["scissors", "scissor", "s"]

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response in paper:
            return "paper"

        elif response in rock:
            return "rock"

        elif response in scissors:
            return "scissors"

        elif response == "xxx":
            return "xxx"

        else:
            print("Please choose from 'rock', 'paper', or 'scissors'. ")


# Main routine
player_move = ""
while player_move != "xxx":

    # ask user for choice, check if its valid
    player_move = user_choice("Choose rock / paper / scissors (r/p/s): ")

    # print output
    if player_move == "xxx":
        break
    else:
        print(f"You chose: {player_move}")

