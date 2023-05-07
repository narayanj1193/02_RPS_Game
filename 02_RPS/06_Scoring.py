
# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Comparison with stats
for item in test_results:
    rounds_played += 1

    # Generate computer choice
    result = item

    if result == "won":
        rounds_won += 1
    elif result == "loss":
        rounds_lost += 1

# rounds drawn
rounds_drawn = rounds_played - rounds_won - rounds_lost

# End of game statement
print()
print("***** End Game Statistics *****")
print(f"Won: {rounds_won} \t|\t Lost: {rounds_lost} \t|\t Draw: {rounds_drawn}")
print()
print("Thanks for playing!")
