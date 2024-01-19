from main import *
from src.lucie_function import *

# Unit Tests
def test_calculate_mission_major():
    assert calculate_mission_major([1, 2, 3, 4, 5], 7) == 40
    assert calculate_mission_major([2, 3, 4, 5, 6], 7) == 40
    assert calculate_mission_major([3, 5, 1, 4, 6], 7) == 30
    assert calculate_mission_major([1, 1, 1, 1, 1], 7) == 50
    assert calculate_mission_major([2, 2, 2, 3, 3], 3) == 6
    assert calculate_mission_major([2, 2, 2, 4, 5], 7) == sum([2, 2, 2, 4, 5])
    assert calculate_mission_major([1, 2, 3, 4], 7) == 30  
    print('TEST OK')
test_calculate_mission_major()

# import unittest
# from main import game 

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

# def test_print_dice():
#     assert print_dice(7)== False
#     assert print_dice("abdejd")== False
#     print("test print dice ok")

# def test_detect_winner()
#     assert detect_winner_game({1:34, 2:56, 3:12]) == "p2"
#     assert detect_winner_game([p1],[34]) == "p1"
#     assert detect_winner_game([p1, p2, p3, p4, p5],[34, 56, 12, 12, 56]) == "p2 & p5"
