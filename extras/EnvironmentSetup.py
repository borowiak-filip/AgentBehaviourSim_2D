"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
class EnvironmentVariables:
    def __init__(self):
        self.obstacle_positions = [(1, 3), (3, 5), (4, 7), (5, 9), (6, 11), (7, 13), (9, 10), (11, 6), (12, 2), (13, 4)]
        self.reward_positions = [(0, 0), (2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (13, 13)]
        self.antiReward_positions = [(13, 5), (13, 12), (12, 10), (12, 5)]
        self.winnable_position = [(14, 14)]
    

    def getObstacles(self) -> list:
        return self.obstacle_positions
    
    def getRewards(self) -> list:
        return self.reward_positions
    
    def getWinnable(self) -> list:
        return self.winnable_position
    
    def getAntiRewards(self) -> list:
        return self.antiReward_positions
       