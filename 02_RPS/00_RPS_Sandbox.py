def user_choice(question):

    paper = ["paper", "p"]
    rock = ["rock", "r"]
    scissors = ["scissors", "scissor", "s"]

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in paper:
            response = "paper"
            return response

        elif response.lower() in rock:
            response = "rock"
            return response

        elif response.lower() in scissors:
            response = "scissors"
            return response

        elif response == "xxx":
            break

        else:
            print("Please choose from 'rock', 'paper', or 'scissors'. ")


# Main routine
player_move = ""
while player_move != "xxx":

    # ask user for choice, check if its valid
    player_move = user_choice("Choose rock / paper / scissors (r/p/s): ")

    # print output
    print(f"You chose: {player_move}")


