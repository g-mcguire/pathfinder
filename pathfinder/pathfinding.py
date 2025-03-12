from pathfinder.generate_matrix import *
from collections import deque

def bfs(matrix):
    if matrix[0][0] == 0:
        return False
    origin = (0,0)
    goal = (len(matrix) - 1, len(matrix) - 1)

    moves = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]

    queue = deque()
    queue.append(origin)

    visited = set()
    visited.add(origin)

    while queue:
    #   get current pos from queue
        coord = queue.popleft()
        if coord == goal:
            return True
        for move in moves:
            new_coord = (coord[0] + move[0], coord[1] + move[1])
            if is_valid_move(matrix, new_coord, visited):
                queue.append(new_coord)
                visited.add(coord)

    return False

def dfs(matrix):
    pass

def is_valid_move(matrix, position, visited):
    # check in bounds
    x, y = position
    bound = len(matrix) - 1
    if not (0 <= x <= bound and 0 <= y <= bound):
        return False
        
    # check dest is 1
    if matrix[x][y] != 1:
        return False
    
    # check not visited
    return position not in visited

# save and return path
