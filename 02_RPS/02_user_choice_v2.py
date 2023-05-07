def user_choice(question):

    # valid inputs:
    valid_list = ["rock", "paper", "scissors", "xxx"]
    error = "That is not a valid input, please enter either rock (r), paper (p), or scissors (s). "

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list, checks the
        else:
            print(error)


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

