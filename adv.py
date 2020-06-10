from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)


# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

"""
# UPER
# There is no destination room
# The goal is to move through every room at least once
# till we get to the end of the room
# When every room has been visited (len(visited) == len(room_graph)) - End (Base Case)
# Then we have gotten to the end of the room
# Nodes/Vertices -> ROOMS
# Edges -> Cardinal Points (Directions (n, s, w, e))

# current_room (begins at starting room which is -> room 0) -> player.current_room
# to move the player into a new_room use -> player.travel(direction)
# to move to a new room -> room.get_room_in_direction(direction)
# path_tracker (Use a list to backtrack path)
# room id -> player.current_room.id
# neighbors (next rooms) -> (Gotten by player.current_room.get_exits())

# player.travel(direction) & room.get_room_in_direction() returns
``` Room 3 -> room id

    (12,16) -> co-ordinates

    Exits: [n, w, e] -> directions list
```
"""
# Expected result -> traversal_path = ['n', 's', etc]
reverse_directions = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w',
}

path_tracker = []
visited = {player.current_room}

# while we haven't visited all 500 rooms
while len(visited) < len(room_graph):
    # Get the current room
    cur_room = player.current_room
    # print('cur room', cur_room)
    # Get the previous room visited
    prev_room = cur_room
    # print('prev room', prev_room)

    # move through every possible exits
    for direction in cur_room.get_exits():  # for each direction
        # Get the next room
        next_room = cur_room.get_room_in_direction(direction)
        # if next room has not been visited
        if next_room not in visited:
            # add to visited
            visited.add(next_room)
            # Move the player to next room
            player.travel(direction)
            # Add the direction to the path tracker
            path_tracker.append(direction)
            # print('path_tracker', path_tracker)
            # Add the direction to the traversal path
            traversal_path.append(direction)
            # print('traversal path forward', traversal_path)
            # Make the current next room the new prev_room
            prev_room = next_room
            # break
            break
    # If we reach the room at the end
    if prev_room == cur_room:
        prev_direction = path_tracker.pop()
        # Get dir to previous room
        dir_to_prev_room = reverse_directions[prev_direction]
        # print('dir_to_prev_room', dir_to_prev_room)
        # move the player to the previous room
        player.travel(dir_to_prev_room)
        # Set the traversal path to follow the reverse directions
        traversal_path.append(dir_to_prev_room)
        # print('traversal path to prev', traversal_path)


# print('current_room', player.current_room)
# print('room id', player.current_room.id)
# print('get_exists', player.current_room.get_exits())

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
