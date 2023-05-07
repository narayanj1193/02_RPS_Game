# Functions at the top
def num_check(question):
    # error code
    error = "Please enter an integer that is more than zero (or <enter> for infinite mode): "

    while True:
        # ask the question
        response = input(question)

        if response != "":
            try:
                # Check that the response is an integer more than zero
                response = int(response)

                # if the amount is too low
                if response > 0:
                    return response

                else:
                    print(error)
            except ValueError:
                print(error)

        return response


# Main routine
rounds_played = 0
instruction = "Please choose rock (r), paper (p), or scissors (s) "

# ask user for # of rounds, <enter> for continuous mode
rounds = num_check("How many rounds would you like to play? <enter> for continuous mode: ")

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played+1}"

    else:
        heading = f"Round {rounds_played+1} of {rounds}"

    print(heading)
    choose = input(f"{instruction} or 'xxx' to end: ")

    if choose == "xxx":
        break

    # Rest of loop
    print(f"You chose {choose}")
    rounds_played += 1

print("Thanks for playing!")
