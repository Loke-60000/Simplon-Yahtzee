
nb_same_dices_value = 0

def detect_yams(roll_dice):
    # Count the occurrences of each value in the dice rolls
    value_counts = {}
    for value in roll_dice:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # Check if any value has occurred 5 times during the same round
    for count in value_counts.values():
        if count >= 5:
            return True

    return False

# Example usage:
assert (player1_dice_rolls = [4, 4, 4, 4, 4]) == True
assert (player2_dice_rolls = [2, 5, 2, 4, 2]) == False

# if detect_yams(player1_dice_rolls):
#     print("Player 1 has a Yams!")
# else:
#     print("Player 1 does not have a Yams.")

# if detect_yams(player2_dice_rolls):
#     print("Player 2 has a Yams!")
# else:
#     print("Player 2 does not have a Yams.")
        