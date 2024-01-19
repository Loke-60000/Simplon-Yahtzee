from main import *
from src.lucie_function import *
import unittest

# Unit Tests
def test_calculate_mission_score():
    assert calculate_mission_score([1, 2, 3, 4, 5], 7) == 40
    assert calculate_mission_score([2, 3, 4, 5, 6], 7) == 40
    assert calculate_mission_score([3, 5, 1, 4, 6], 7) == 30
    assert calculate_mission_score([1, 1, 1, 1, 1], 7) == 50
    assert calculate_mission_score([2, 2, 2, 3, 3], 7) == 25
    assert calculate_mission_score([2, 2, 2, 2, 5], 8) == 8
    assert calculate_mission_score([1, 2, 3, 4], 7) == 30
    assert calculate_mission_score([2, 2, 2, 3, 3], 4) == 6
    print('TEST calculate_mission OK')
test_calculate_mission_score()

# class TestYahtzeeGame(unittest.TestCase):

#     def test_winner(self):
#         # Simulate a game with predefined player actions
#         player_actions = [
#             "3",  # number of players
#             # Player 1
#             "retry 1,2,3", "retry 4,5", "", "1",
#             # Player 2
#             "retry 2,3,5", "", "", "2",
#             # Player 3
#             "retry 2,3,5", "retry", "", "1",
#         ]

#         with unittest.mock.patch('builtins.input', side_effect=player_actions):
#             winner = game()
        
#         # Check if the winner is one of the players
#         seassertIn(winner, [1, 2])

# if __name__ == '__main__':
#     unittest.main()

# def test_detect_winner()
#     assert detect_winner_game({1:34, 2:56, 3:12]) == "p2"
#     assert detect_winner_game([p1],[34]) == "p1"
#     assert detect_winner_game([p1, p2, p3, p4, p5],[34, 56, 12, 12, 56]) == "p2 & p5"
