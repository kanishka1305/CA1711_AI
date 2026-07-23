from collections import deque

goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

# Find blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next states
def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(row) for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            neighbors.append(tuple(tuple(row) for row in new))

    return neighbors

# BFS
def bfs(start):
    queue = deque([(start, 0)])   # (state, moves)
    visited = set()

    while queue:
        state, moves = queue.popleft()

        if state == goal:
            return moves, state

        if state not in visited:
            visited.add(state)

            for neighbor in get_neighbors(state):
                queue.append((neighbor, moves + 1))

    return None

# Main
start = ((1,2,3),
         (4,0,6),
         (7,5,8))

result = bfs(start)

if result:
    moves, solved = result

    print("Goal State Reached!")
    print("Number of Moves:", moves)
    print("\nSolved Puzzle:")

    for row in solved:
        print(row)
else:
    print("No Solution")
