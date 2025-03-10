import numpy as np
import re
import json
import base64

def _parse_map(map_string, map_size, reversal_nodes=[]):
    width, height = map_size
    decoded_string = base64.b64decode(map_string).decode('utf-8')
    filtered_chars = re.sub(r'[^a-zA-Z]', '', decoded_string)
    
    binary_values = [bin(ord(c))[2:].zfill(8) for c in filtered_chars]
    
    map_data = []
    for binary_value in binary_values:
        first_half = int(binary_value[:4], 2)
        second_half = int(binary_value[4:], 2)
        map_data.extend([first_half % 2, second_half % 2])
    
    while len(map_data) < width * height:
        map_data.append(0)
    
    map_data = map_data[:width * height]
    
    grid = np.array(map_data).reshape((height, width))
    
    for x, y in reversal_nodes:
        if 0 <= x < width and 0 <= y < height:
            grid[y, x] = 1 - grid[y, x]
    
    return grid

def _load_maze_from_json(maze_level_name):
    with open(f"./src/game/maze_level/{maze_level_name}.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    maze_level_name = data.get("maze_level_name", "Unknown Level")
    map_size = tuple(data.get("map_size", [10, 10]))
    starting_position = tuple(data.get("starting_position", [0, 0]))
    end_position = tuple(data.get("end_position", [0, 0]))
    map_string = data.get("map", "")
    reversal_nodes = data.get("reversal_node", [])
    
    parsed_map = _parse_map(map_string, map_size, reversal_nodes)
    
    return {
        "maze_level_name": maze_level_name,
        "map_size": map_size,
        "starting_position": starting_position,
        "end_position": end_position,
        "map": parsed_map
    }

def hit_obstacle(position, maze_level_name):
    x, y = position
    maze_data = _load_maze_from_json(maze_level_name)
    grid = maze_data["map"]
    
    # Check if the position is within the bounds of the grid
    if 0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]:
        # Return True if there's an obstacle (1) at the position, False if free space (0)
        return grid[y, x] == 1
    else:
        # Position is out of bounds
        return True

def game_over(health):
    return health == 0 or health == 666

def arrive_at_destination(maze_level_name, current_position):
    maze_data = _load_maze_from_json(maze_level_name)
    end_position = maze_data["end_position"]
    return tuple(current_position) == end_position
