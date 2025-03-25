# -*- coding: utf-8 -*-

"""Problem 1: Emergency Pathfinding using BFS"""
from collections import deque

def locate_escape_path(layout, origin, destination):
    rows, cols = len(layout), len(layout[0])
    moves = [(-1,0), (0,1), (1,0), (0,-1)]  # Up, Right, Down, Left
    frontier = deque([(origin[0], origin[1], 0, [])])
    explored = set(origin)

    while frontier:
        y, x, count, route = frontier.popleft()

        if (y, x) == destination:
            route.append((y, x))
            display_path(layout, route)
            return f"Emergency route found in {count} moves! Path: {route}"

        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and layout[ny][nx] != 1 and (ny, nx) not in explored:
                frontier.append((ny, nx, count + 1, route + [(y, x)]))
                explored.add((ny, nx))

    return "No viable escape route!"

def display_path(grid, path):
    """Visualize path on grid layout"""
    grid_copy = [row.copy() for row in grid]
    for y, x in path:
        grid_copy[y][x] = '→'
    
    print("\nEmergency Path Visualization:")
    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))
    print()

# Grid configuration (0=clear, 1=blocked, S=start, D=destination)
building_layout = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    ['S', 1, 0, 'D', 0]
]

# Locate start and destination points
start_pos = dest_pos = None
for idx, row in enumerate(building_layout):
    if 'S' in row:
        start_pos = (idx, row.index('S'))
        row[start_pos[1]] = 0
    if 'D' in row:
        dest_pos = (idx, row.index('D'))
        row[dest_pos[1]] = 0

if start_pos and dest_pos:
    print(locate_escape_path(building_layout, start_pos, dest_pos))
else:
    print("Missing start or destination point!")

"""Problem 2: Tunnel Depth Analysis using DFS"""
from collections import defaultdict

class TunnelExplorer:
    def __init__(self):
        self.network = defaultdict(list)
        self.max_path = []
        self.max_level = 0

    def connect(self, a, b):
        self.network[a].append(b)
        self.network[b].append(a)

    def depth_search(self, current, visited, track, level):
        visited.add(current)
        track.append(current)

        if level > self.max_level:
            self.max_level = level
            self.max_path = track.copy()

        for adjacent in self.network[current]:
            if adjacent not in visited:
                self.depth_search(adjacent, visited, track, level+1)

        track.pop()
        visited.remove(current)

    def find_deepest(self, entrance):
        visited_nodes = set()
        self.depth_search(entrance, visited_nodes, [], 0)
        return self.max_path, self.max_level

tunnel_system = TunnelExplorer()
tunnel_system.connect(1, 2)
tunnel_system.connect(1, 3)
tunnel_system.connect(2, 4)
tunnel_system.connect(2, 5)
tunnel_system.connect(3, 6)
tunnel_system.connect(5, 7)
tunnel_system.connect(5, 8)
tunnel_system.connect(7, 9)

deepest_route, depth = tunnel_system.find_deepest(1)
print(f"Deepest pathway: {deepest_route}\nDepth level: {depth}")

"""Problem 3: Optimal Shipping Routes using Dijkstra's Algorithm"""
import heapq

class LogisticsNetwork:
    def __init__(self):
        self.connections = {}

    def add_connection(self, city_a, city_b, km):
        if city_a not in self.connections:
            self.connections[city_a] = []
        if city_b not in self.connections:
            self.connections[city_b] = []
        
        self.connections[city_a].append((km, city_b))
        self.connections[city_b].append((km, city_a))

    def compute_routes(self, start_city):
        priority_queue = [(0, start_city)]
        distances = {city: float('inf') for city in self.connections}
        distances[start_city] = 0

        while priority_queue:
            current_km, current = heapq.heappop(priority_queue)
            
            for km, neighbor in self.connections[current]:
                if (new_km := current_km + km) < distances[neighbor]:
                    distances[neighbor] = new_km
                    heapq.heappush(priority_queue, (new_km, neighbor))
        
        return distances

delivery_network = LogisticsNetwork()
delivery_network.add_connection("A", "B", 50)
delivery_network.add_connection("A", "C", 30)
delivery_network.add_connection("B", "D", 70)
delivery_network.add_connection("C", "D", 40)
delivery_network.add_connection("C", "E", 60)
delivery_network.add_connection("D", "F", 20)
delivery_network.add_connection("E", "F", 50)
delivery_network.add_connection("B", "E", 90)

optimal_routes = delivery_network.compute_routes("A")
print("Optimal delivery distances from City A:")
for city, distance in optimal_routes.items():
    print(f"{city}: {distance}km")

"""Problem 4: Tic-Tac-Toe AI using Minimax"""
import math

BOT = 'X'
OPPONENT = 'O'
EMPTY = ' '

def game_state(board):
    win_patterns = [(0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6)]
    
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    
    return "Tie" if EMPTY not in board else None

def calculate_score(board):
    result = game_state(board)
    return 10 if result == BOT else -10 if result == OPPONENT else 0

def minimax_strategy(board, depth, is_max):
    current_score = calculate_score(board)
    
    if current_score in (10, -10) or EMPTY not in board:
        return current_score
    
    if is_max:
        best = -math.inf
        for pos in range(9):
            if board[pos] == EMPTY:
                board[pos] = BOT
                best = max(best, minimax_strategy(board, depth+1, False))
                board[pos] = EMPTY
        return best
    else:
        best = math.inf
        for pos in range(9):
            if board[pos] == EMPTY:
                board[pos] = OPPONENT
                best = min(best, minimax_strategy(board, depth+1, True))
                board[pos] = EMPTY
        return best

def optimal_move(current_board):
    best_score = -math.inf
    move = -1
    
    for i in range(9):
        if current_board[i] == EMPTY:
            current_board[i] = BOT
            score = minimax_strategy(current_board, 0, False)
            current_board[i] = EMPTY
            
            if score > best_score:
                best_score = score
                move = i
                
    return move

# Test board configuration
game_board = ['', 'O', 'X',
              ' ', '', ' ',
              ' ', ' ', 'X']

best_position = optimal_move(game_board)
print(f"Optimal AI move: Position {best_position}")