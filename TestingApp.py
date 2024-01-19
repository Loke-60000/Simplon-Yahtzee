from main import *
from src.lucie_function import *
import unittest
import random

# Unit Tests
def test_calculate_mission_score():
    assert calculate_mission_score([1, 2, 3, 4, 5], 7) == 40
    assert calculate_mission_score([1, 2, 3, 4, 5], 3) == 0
    assert calculate_mission_score([2, 3, 4, 5, 6], 7) == 40
    assert calculate_mission_score([3, 5, 1, 4, 6], 7) == 30
    assert calculate_mission_score([1, 1, 1, 1, 1], 7) == 50
    assert calculate_mission_score([2, 2, 2, 3, 3], 7) == 25
    assert calculate_mission_score([2, 2, 2, 2, 5], 8) == 8
    assert calculate_mission_score([1, 2, 3, 4, 6], 7) == 30
    assert calculate_mission_score([2, 2, 2, 3, 3], 4) == 6
    assert calculate_mission_score([2, 2, 2, 3, 4], 3) == 6
    print('First_test: OK!')
test_calculate_mission_score()

def test_reroll_dice():
    
    # Cas de test 1 : Relancer un dé unique
    dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [2]
    reroll_dice(dice_values, reroll_indices)
    assert 1 <= dice_values[2] <= 6

    # Cas de test 2 : Relancer plusieurs dés
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [0, 2, 4]
    reroll_dice(original_dice_values, reroll_indices)
    for i in reroll_indices:
        assert 1 <= original_dice_values[i] <= 6
    # Cas de test 3 : Aucun dé à relancer
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = []
    reroll_dice(original_dice_values, reroll_indices)
    assert original_dice_values == [1, 2, 3, 4, 5]

    # Cas de test 4 : Tous les dés à relancer
    original_dice_values = [1, 2, 3, 4, 5]
    reroll_indices = [0, 1, 2, 3, 4]
    reroll_dice(original_dice_values, reroll_indices)
    for i in reroll_indices:
        assert 1 <= original_dice_values[i] <= 6
    print('Second_Test: OK!')
# Exécutez les tests
test_reroll_dice()