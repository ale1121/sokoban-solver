from search_methods.solver import Solver
from search_methods.node import Node
from sokoban import Map
from sokoban.moves import *
import math

class IDAStar(Solver):
    def __init__(self, map: Map, pull_cost=1.5) -> None:
        super().__init__(map, pull_cost)
        self.dist_map = [[{} for _ in range(map.width)] for _ in range(map.length)]
        self.compute_goal_dist(map)

    def ida_star(self, start):
        threshold = self.heuristic(start)
        while True:
            temp = self.search(start, 0, threshold)
            if isinstance(temp, Node):
                return temp
            if temp == math.inf:
                return None
            threshold = temp

    def search(self, node, g, threshold, visited=set()):
        if node.h == math.inf:
            return math.inf

        f = g + node.h
        if f > threshold:
            return f
        if node.is_solved():
            return node

        visited.add(node)

        self.explored_states += 1

        min_threshold = math.inf

        neighbours = node.get_neighbours()
        for neighbour in neighbours:
            neighbour.h = self.heuristic(neighbour)

        neighbours = sorted(neighbours, key=lambda x: x.h)

        for neighbour in neighbours:
            if neighbour in visited:
                continue
            
            cost = 1 if neighbour.map.undo_moves == node.map.undo_moves else self.pull_cost
            temp = self.search(neighbour, g + cost, threshold, visited)
            
            if isinstance(temp, Node):
                return temp
            if temp < min_threshold:
                min_threshold = temp

        visited.remove(node)
        return min_threshold

    def solve(self):
        self.explored_states = 0

        h = self.heuristic(self.start_node)
        self.start_node.h = h

        self.final_node = self.ida_star(self.start_node)
        if self.final_node:
            return self.final_node.map, self.explored_states, self.final_node.map.undo_moves
        else:
            return None, self.explored_states, math.inf
