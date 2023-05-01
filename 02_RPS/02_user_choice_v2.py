# Functions go at the top
def choice_checker(question):

    error = "Please choose from rock / paper / scissors (r/p/s). Or use 'xxx' to quit."

    while True:

        # Ask user for choice
        response = input(question).lower

        if response == "rock" or response == "r":
            return response

        elif response == "scissors" or response == "s":
            return response

        elif response == "paper" or response == "p":
            return response

        # check for error code
        elif response == "xxx":
            return response
        else:
            print(error)


# Main routine

# Ask user for their choice
user_choice = ""
while user_choice != "xxx":

    # ask user for choice, check if its valid
    user_choice = choice_checker("\nChoose rock / paper / scissors (r/p/s): ")

    # print output
    print(f"You chose: {user_choice}")

