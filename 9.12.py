import numpy as np
import pandas as pd

data = pd.read_csv('Inputs/Day 9.txt', names=['dir', 'dis'], dtype={'dir': str, 'dis': 'Int64'}, sep=' ')


def move_head(direction, location):    # method to move the rope head
    if direction == 'L':
        new_x = location[1]-1
        new_y = location[0]
    elif direction == 'R':
        new_x = location[1]+1
        new_y = location[0]
    elif direction == 'U':
        new_x = location[1]
        new_y = location[0]-1
    elif direction == 'D':
        new_x = location[1]
        new_y = location[0]+1
    new_loc = [new_y, new_x]
    return new_loc  # incrementing the coordinates depending on the direction


def move_tail(head_pos, location):  # method to move the rope tail
    if abs(head_pos[0]-location[0]) + abs(head_pos[1]-location[1]) == 1 \
            or abs(head_pos[0]-location[0]) - abs(head_pos[1]-location[1]) == 0:
        return location  # if the tail is within one block of the head then it does not need to move
    elif not location[0]-head_pos[0] == 0 and not location[1]-head_pos[1] == 0:
        new_x = location[1]+((head_pos[1]-location[1])/abs(head_pos[1]-location[1]))  # if the tail is not within one
        new_y = location[0]+((head_pos[0]-location[0])/abs(head_pos[0]-location[0]))  # block of the head it moves one
        # space in both directions
    elif location[0]-head_pos[0] == 0:  # moving in x
        new_x = location[1] + ((head_pos[1] - location[1]) / abs(head_pos[1] - location[1]))
        new_y = location[0]
    elif location[1]-head_pos[1] == 0:  # moving in y
        new_x = location[1]
        new_y = location[0] + ((head_pos[0] - location[0]) / abs(head_pos[0] - location[0]))
    new_loc = [int(new_y), int(new_x)]
    return new_loc


def move_knot(knot_pos, location):   # method to move the knots
    if knot_pos == location:
        return location  # If the knots overlap they do not need to move
    elif abs(knot_pos[0] - location[0]) + abs(knot_pos[1] - location[1]) == 1:
        return location  # if the knot is within one block of the prev knot then it does not need to move
    elif abs(knot_pos[0] - location[0]) - abs(knot_pos[1] - location[1]) == 0 and abs(knot_pos[0] - location[0]) == 1:
        return location  # if the knot is within one block diagonally of the prev knot then it does not need to move
    elif abs(knot_pos[0] - location[0]) - abs(knot_pos[1] - location[1]) == 0 \
            and not abs(knot_pos[0] - location[0]) == 1:
        new_x = location[1]+((knot_pos[1] - location[1]) / abs(knot_pos[1] - location[1]))
        new_y = location[0]+((knot_pos[0] - location[0]) / abs(knot_pos[0] - location[0]))
        new_loc = [int(new_y), int(new_x)]  # if the previous knot moved diagonally
        return new_loc
    elif not location[0] - knot_pos[0] == 0 and not location[1] - knot_pos[1] == 0:
        new_x = location[1]+((knot_pos[1] - location[1]) / abs(knot_pos[1] - location[1]))  # if the tail is not within
        new_y = location[0]+((knot_pos[0] - location[0]) / abs(knot_pos[0] - location[0]))  # one block of the head it
        # moves one space in either or both directions
    elif location[0]-knot_pos[0] == 0:
        new_x = location[1] + ((knot_pos[1] - location[1]) / abs(knot_pos[1] - location[1]))
        new_y = location[0]
    elif location[1]-knot_pos[1] == 0:
        new_x = location[1]
        new_y = location[0] + ((knot_pos[0] - location[0]) / abs(knot_pos[0] - location[0]))
    new_loc = [int(new_y), int(new_x)]
    return new_loc


# initialize the board
# upper bound for the field size is up+down by left+right
# create the field
sum_up = 0
sum_down = 0
sum_left = 0
sum_right = 0
i = 0
while i < len(data):
    distance = data.at[i, 'dis']
    if data.at[i, 'dir'] == 'L':
        sum_left += distance
    elif data.at[i, 'dir'] == 'R':
        sum_right += distance
    if data.at[i, 'dir'] == 'U':
        sum_up += distance
    if data.at[i, 'dir'] == 'D':
        sum_down += distance
    i += 1

tailTrackGrid = np.zeros((sum_down+sum_up, sum_left+sum_right))
current_loc = [sum_up, sum_right]
tail_loc = current_loc
tailTrackGrid[tail_loc[0], tail_loc[1]] = 1

j = 0   # loop for moving the rope
while j < len(data):
    k = 0
    while k < data.at[j, 'dis']:
        next_loc = move_head(data.at[j, 'dir'], current_loc)    # moves the head of the rope
        new_tail_loc = move_tail(next_loc, tail_loc)    # moves the tail of the rope
        tailTrackGrid[new_tail_loc[0], new_tail_loc[1]] = 1  # changes the value of the space where the tail is to 1
        current_loc = next_loc
        tail_loc = new_tail_loc
        k += 1
    j += 1
print('Part 1:')
print('The number spaces the tail has visited is ' + str(np.count_nonzero(tailTrackGrid == 1)))  # counts all spaces = 1

# Part 2
# tails can follow tails now -> diagonal movement is possible. Addressed in move_knot
# initializing the board, 1 head 9 nodes
tailTrackGrid = np.zeros((sum_down+sum_up, sum_left+sum_right))
current_loc = [sum_up, sum_right]
knot1 = current_loc
knot2 = current_loc
knot3 = current_loc
knot4 = current_loc
knot5 = current_loc
knot6 = current_loc
knot7 = current_loc
knot8 = current_loc
tail_loc = current_loc
tailTrackGrid[tail_loc[0], tail_loc[1]] = 1

m = 0   # loop for moving the rope and knots
while m < len(data):
    n = 0
    while n < data.at[m, 'dis']:
        next_loc = move_head(data.at[m, 'dir'], current_loc)    # moves the head of the rope
        knot1 = move_tail(next_loc, knot1)
        knot2 = move_knot(knot1, knot2)
        knot3 = move_knot(knot2, knot3)
        knot4 = move_knot(knot3, knot4)
        knot5 = move_knot(knot4, knot5)
        knot6 = move_knot(knot5, knot6)
        knot7 = move_knot(knot6, knot7)
        knot8 = move_knot(knot7, knot8)
        new_tail_loc = move_knot(knot8, tail_loc)    # moves the tail of the rope
        tailTrackGrid[new_tail_loc[0], new_tail_loc[1]] = 1  # changes the value of the space where the tail is to 1
        current_loc = next_loc
        tail_loc = new_tail_loc
        n += 1
    m += 1
print('Part 2:')
print('The number spaces the tail has visited is ' + str(np.count_nonzero(tailTrackGrid == 1)))  # counts all spaces = 1
