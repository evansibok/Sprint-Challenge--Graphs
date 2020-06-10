from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)


# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print('starting room', world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


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
# path_to_room (use a Queue to monitor and track back) -> Queue
# room id -> player.current_room.id
# neighbors (possible rooms) -> (Gotten by player.current_room.get_exits())
# visited to track visited rooms -> set()

# player.travel(direction) & room.get_room_in_direction() returns
``` Room 3 -> room id

    (12,16) -> co-ordinates

    Exits: [n, w, e] -> directions list
```
"""
# Expected result -> traversal_path = ['n', 's', etc]
reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
# Initialize a Queue
q = deque()
backtrack = deque()
# Initialize visited set
visited = set()
# Get starting room
# Push the starting room path to the Queue
q.append([player.current_room])
# While the Queue is not empty
while len(visited) < len(room_graph):
    # Set the last room visited to enable backtracking
    last_room = player.current_room
    # Dequeue the starting room path from the queue
    path = q.popleft()
    # Get the current room from the dequeued path
    cur_room = path[-1]
    # for each directions in next rooms
    for direction in cur_room.get_exits():
        # get each next room
        next_room = cur_room.get_room_in_direction(direction)
        # if next room is not visited
        if next_room not in visited:
            # Add next room to visited
            visited.add(next_room)
            # Move player to next room
            player.travel(direction)
            # add "direction to current room" to backtrack path
            backtrack.append(reverse_direction[direction])
            # add "direction to current room" to traversal path
            traversal_path.append(direction)
            # add the next room path to the initial path
            forward_path = [path] + [next_room]
            # append this cp to the queue
            q.append(forward_path)
            # set that exit room as the last room visited
            last_room = next_room


# if cur_room == initial_room:
#     prev_room = cur_room.get_room_in_direction(
#         reverse_direction[direction])
#     backtrack = path + [prev_room]
#     player.travel(reverse_direction[direction])
#     traversal_path.append(reverse_direction[direction])
#     q.append(backtrack)

# print('current_room', player.current_room)
# print('room id', player.current_room.id)
# print('get_exists', player.current_room.get_exits())


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# for direction in player.current_room.get_exits():
#     if direction == "n":
#         print('get_room_in_d', player.current_room.get_room_in_direction(direction))
#     if direction == "s":
#         print('get_room_in_d', player.current_room.get_room_in_direction(direction))
#     if direction == "w":
#         print('get_room_in_d', player.current_room.get_room_in_direction(direction))
#     if direction == "e":
#         print('get_room_in_d', player.current_room.get_room_in_direction(direction))


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
