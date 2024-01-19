from main import roll_dice, calculate_points, reroll_dice, get_reroll_indices

def test_roll_dice():
    dice_values = roll_dice(5)
    assert len(dice_values) == 5, "roll_dice should return 5 dice values"
    for value in dice_values:
        assert 1 <= value <= 6, f"Dice value {value} should be between 1 and 6"

def test_calculate_points():
    assert calculate_points([3, 3, 3, 4, 5]) == 9, "calculate_points should return 9 for [3, 3, 3, 4, 5]"
    unique_dice_test = calculate_points([1, 2, 3, 4, 5])
    assert unique_dice_test in [1, 2, 3, 4, 5], "calculate_points should return a value from the dice [1, 2, 3, 4, 5]"

def test_reroll_dice():
    # Initial roll
    dice_values = roll_dice(5)
    # Copy the original dice values
    original_values = list(dice_values)
    # Choose a die to reroll (for simplicity, always reroll the first die)
    reroll_indices = [0]
    reroll_dice(dice_values, reroll_indices)
    # Check if the rerolled die has a different value
    assert dice_values[0] != original_values[0], "The rerolled die should have a different value"

def test_get_reroll_indices():
    assert get_reroll_indices("retry 1, 3, 5") == [0, 2, 4], "get_reroll_indices should return [0, 2, 4] for 'retry 1, 3, 5'"
    assert get_reroll_indices("retry 1,3,5") == [0, 2, 4], "get_reroll_indices should return [0, 2, 4] for 'retry 1,3,5'"
    assert get_reroll_indices("retry") == [], "get_reroll_indices should return an empty list for 'retry'"

def run_tests():
    test_roll_dice()
    test_calculate_points()
    test_reroll_dice()
    test_get_reroll_indices()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()