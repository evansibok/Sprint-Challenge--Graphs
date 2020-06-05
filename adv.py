from room import Room
from player import Player
from world import World
from util import Stack

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


def move_through_rooms(room, visited=None):
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
    # to move to new_room use -> player.travel(direction)
    # path_to_room (use a stack to monitor and track back) -> Stack
    # room id -> player.current_room.id
    # neighbors (possible rooms) -> (Gotten by player.current_room.get_exits())
    # visited to track visited rooms -> set()
    """
    pass


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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


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
