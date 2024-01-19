from main import reroll_dice
import random

def test_reroll_dice():
    
    # Cas de test 1 : Relancer un dé unique
    dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [2]
    reroll_dice(dice_values, reroll_indices)
    assert 1 <= dice_values[2] <= 6
    print("test OK")

    # Cas de test 2 : Relancer plusieurs dés
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [0, 2, 4]
    reroll_dice(original_dice_values, reroll_indices)
    for i in reroll_indices:
        assert 1 <= original_dice_values[i] <= 6
    print("test OK")

    # Cas de test 3 : Aucun dé à relancer
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = []
    reroll_dice(original_dice_values, reroll_indices)
    assert original_dice_values == [1, 2, 3, 4, 5]
    print("test OK")

    # Cas de test 4 : Tous les dés à relancer
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [0, 1, 2, 3, 4]
    reroll_dice(original_dice_values, reroll_indices)
    for i in reroll_indices:
        assert 1 <= original_dice_values[i] <= 6
    print("test OK")

# Exécutez les tests
test_reroll_dice()
