import pandas as pd
import numpy as np


class Graph:    # building a graph of nodes towards the goal
    def __init__(self):
        self.nodes = []

    def add_node(self, node):   # adding a node to the graph
        self.nodes.append(node)

    def get_path_length(self, parents, loc):    # getting all parents of a given node, back to the start
        self.nodes[loc].get_path_length(parents)
        return parents


class Node:  # every space visited becomes a node, chained towards the end
    def __init__(self, parent, height, y_loc, x_loc):
        self.parent = parent
        self.height = height
        self.y_loc = y_loc
        self.x_loc = x_loc

    def get_path_length(self, parents):  # recursively going up the line of parents until you reach the start
        if self.parent is None:
            print('The length of the path is ' + str(len(parents)))
            return parents
        else:
            parents.append(self.parent)
            parents.append(self.parent.get_path_length(parents))


data = pd.read_csv('Inputs/Day 12.txt', header=None, dtype=str)
grid = []
i = 0
while i < len(data):    # parsing the input into a grid of numbers
    j = 0
    new_line = []
    while j < len(data.iat[0, 0]):
        new_line.extend(data.iat[i, 0][j])
        new_line[j] = ord(new_line[j]) - 96  # changing each letter at the gridspace to its place in the alphabet
        j += 1
    if len(grid) > 0:
        grid = np.vstack((grid, new_line))  # building the grid
    else:
        grid = new_line
    i += 1
start = np.where(grid == -13)  # starting position
end = np.where(grid == -27)  # ending position
grid[start] = 1
grid[end] = 26
visited_grid = np.zeros(grid.shape)
l = 0

graph = Graph()
start_node = Node(None,grid[start], start[0], start[1])
graph.add_node(start_node)
visited_grid[start] = 1
stepNumber = 0
while True:
    for m in graph.nodes:
        y = m.y_loc
        x = m.x_loc
        if y > 0:
            if visited_grid[y - 1, x] == 0:
                if grid[y - 1, x] - m.height <= 1:
                    graph.add_node(
                        Node(m, grid[y - 1, x], y - 1, x))
                    visited_grid[y - 1, x] = 1
                    if [y - 1, x] == [end[0], end[1]]:
                        break
        if x > 0:
            if visited_grid[y, x - 1] == 0:
                if grid[y, x - 1] - m.height <= 1:
                    graph.add_node(
                        Node(m, grid[y, x - 1], y, x - 1))
                    visited_grid[y, x - 1] = 1
                    if [y, x - 1] == [end[0], end[1]]:
                        break
        if y < grid.shape[0] - 1:
            if visited_grid[y + 1, x] == 0:
                if grid[y + 1, x] - m.height <= 1:
                    graph.add_node(
                        Node(m, grid[y + 1, x], y + 1, x))
                    visited_grid[y + 1, x] = 1
                    if [y + 1, x] == [end[0], end[1]]:
                        break
        if x < grid.shape[1] - 1:
            if visited_grid[y, x + 1] == 0:
                if grid[y, x + 1] - m.height <= 1:
                    graph.add_node(
                        Node(m, grid[y, x + 1], y, x + 1))
                    visited_grid[y, x + 1] = 1
                    if [y, x + 1] == [end[0], end[1]]:
                        break
        stepNumber += 1
    if visited_grid[end] == 1:
        break
graph.get_path_length([], -1)    # starting at the ending node, going back up the chain of parents until the start
