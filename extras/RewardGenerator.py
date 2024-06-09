"""
Author: Filip Borowiak
Date: Sunday 9th of June 2024
"""
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def generate_reward_positions(winnable_position, grid_size):
    reward_positions = []
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if (x, y) != winnable_position:
                value = 1 / manhattan_distance(winnable_position, (x, y))
                if  value > 0.05:
                    reward_positions.append((x, y, value))
            else:
                continue 
            
    return reward_positions
