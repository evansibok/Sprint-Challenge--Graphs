from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)


# ROOMS SAMPLE
"""
{
  494: [(1, 8), {'e': 457}],
  492: [(1, 20), {'e': 400}],
  493: [(2, 5), {'e': 478}],
  457: [(2, 8), {'e': 355, 'w': 494}],
  484: [(2, 9), {'n': 482}],
  482: [(2, 10), {'s': 484, 'e': 404}],
}
"""


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
# to move to new_room use -> player.travel(direction) or room.get_room_in_direction(direction)
# path_to_room (use a stack to monitor and track back) -> Stack
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
# Initialize a Stack
s = deque()
# Initialize visited set
visited = set()
# Get starting room
# Push the starting room path to the stack
print('current room', player.current_room)
s.append([player.current_room])
# While the stack is not empty
while len(s) > 0:
    # Pop the starting room from the path
    path = s.pop()
    # Get the direction of the starting room
    # if path is not None:
    cur_room = path[-1]
    print('cur_room', cur_room)
    # if current room not in visited
    if cur_room not in visited:
        # if len(visited rooms) == len(room_graph) -> base case -> return path
        # add current room to visited
        visited.add(cur_room)
        # get next rooms
        for next in cur_room.get_exits():
            # append next rooms path to the current room
            copied = path + [cur_room.get_room_in_direction(next)]
            # print('copied', copied)
            # and push to stack
            s.append(copied)

    # print('current_room', starting_room)
    # print('room id', starting_room.id)
    # print('get_exists', starting_room.get_exits())


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
