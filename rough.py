1 [2] -> [e(2)] - -e back[]
2 [3, 4] -> [n(4)] -> for[e - n(4)] - - e, n back[s] -> for[e - n - s - e(3)]
4 [] -> No next room, back[s(2)]
3 [] -> No next room, back[w(2)] -> e, n, s, e, w, w


1 - 2 - 3
| |
4   5

bfs
[1] -> 1 -> is 1 in visited,
yes(exit)
No -> add it to visited -> get the next rooms(2)
-> get path to the next room -> [2]
-> append it to the initial path[1] + [2] -> appended_path = [1, 2]
-> get the direction[e(2)]
-> append to traversal_path -> [e]
-> append the appended_path to the Queue[1, 2]

[1, 2] -> 2 -> is 2 in visited,
yes(exit)
No -> add it to visited -> get the next rooms(3, 4)
-> get path to each individual next room -> [3], [4]
-> append each individual next room to the initial path
-> [1, 2] + [3] -> appended_path = [1, 2, 3]
-> Get the direction to room 3 [e(3)]
-> append to traversal_path -> [e, e]
-> append the appended_path to the Queue[1, 2, 3]


when you find the split into rooms 3 and 4

you cannot directly append to the traversal path right now

but you need to backtrack first from room 3, then go room 4

and the way you know you'll need to backtrack is that room 3 has no unvisited exits

so that means its time to go back, check if there are any unvisited exits, which there is the room 4


# Get current room (2)
# for each directions in next rooms [e, n]
# get each next room
e -> 3, n -> 4
# if next room is not in visited
if 3 not in visited
# add it to visited
visited.add(3)
# add the direction to current room to backtrack path
backtrack.append(e)
# add the direction to current room to traversal path
traversal_path.append(e)
# add the next room path to the initial path
cp = [path] + [next_room]
# append this cp to the queue
q.append(cp)

# move the player to that exit room
# set that exit room as the last room visited
#


-> [1, 2] + [4] -> appended_path = [1, 2, 4]
-> Get the direction to room 4 [n(4)]
-> append to traversal_path -> [e, n], How will[e, e] and [e, n] come together? Maybe save a temporary traversal_path in a queue so when we have multiple rooms, we can do bfs on it to move to an individual room and save the path to the main traversal_path
-> append the appended_path to the Queue[1, 2, 4]
