import random


# checks if users choice is valid, and returns move.
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


# get computer move
def get_computer_move():
    move = random.choice(rps_list[:-1])
    return move


# checks for valid amount of rounds
def num_check(question):
    # error code
    error = "Please enter an integer that is more than zero (or <enter> for infinite mode)\n "

    while True:
        # ask the question
        response = input(question)

        if not response:
            # Return None for infinite mode
            return None

        try:
            # Check that the response is an integer more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Main routine
rounds_played = 0
rounds_won = 0
rounds_lost = 0
rounds_drawn = 0

game_summary = []

instruction = "Please choose rock (r), paper (p), or scissors (s) "

# ask user for # of rounds, <enter> for continuous mode
rounds = num_check("How many rounds would you like to play? <enter> for continuous mode: ")

while True:
    rounds_played += 1

    # Checks if the requested number of rounds has been met, if so break the code.
    if rounds is not None and rounds_played == rounds + 1:
        break

    # Rounds Heading
    print()
    if rounds is None:
        heading = f"Continuous Mode: Round {rounds_played}"

    else:
        heading = f"Round {rounds_played} of {rounds}"
    print(heading)

    # Ask user for their choice of move (rock, paper, or scissors + xxx)
    user_move = user_choice(f"{instruction} or 'xxx' to end: ")

    # exit code
    if user_move == "xxx":
        break

    # get computer choice
    comp_move = get_computer_move()

    # winning combinations for move comparison
    winning_combinations = {'rock': 'scissors', 'paper': 'rock',
                            'scissors': 'paper'}

    # compare moves
    if user_move == comp_move:
        result = "tie"
        feedback = "drew"

    elif winning_combinations[user_move] == comp_move:
        result = "won"
        rounds_won += 1

    else:
        result = "lost"
        rounds_lost += 1

    feedback = f"{user_move} vs {comp_move} - you {result}"

    # rounds drawn
    rounds_drawn = rounds_played - rounds_won - rounds_lost

    # output player move
    print(f"\nYou chose: {user_move}.\nCOM chose: {comp_move}. \n{feedback}")

    # outcome variable for game summary
    outcome = f"Round {rounds_played}: {result}"
    game_summary.append(outcome)

# Calculate amount of draws
rounds_drawn = rounds_played - rounds_lost - rounds_won - 1

# Calculate Game Stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("**** Game History ****")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the
print("***** Game Statistics *****")
print("Wins: {} ({:.0f}%) \nLosses: {} ({:.0f}%) \nTie: {} ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                                                             percent_lose, rounds_drawn,
                                                                             percent_tie))
print()
print("Thanks for Playing!")
print()
