from search_methods.solver import Solver
from search_methods.node import Node
from sokoban import Map
from sokoban.moves import *
import math

class BeamSearch(Solver):
    def __init__(self, map: Map, pull_cost : float = 10, beam_width=70) -> None:
        super().__init__(map, pull_cost)
        self.beam_width = beam_width
        self.dist_map = [[{} for _ in range(map.width)] for _ in range(map.length)]
        self.compute_goal_dist(map)

    def heuristic(self, node: Node) -> float:
        h = super().heuristic(node)
        h += node.map.undo_moves * self.pull_cost
        return h

    def beam_search(self, start):
        open = [start]
        visited = set()
        visited.add(start)

        while open:
            successors = []

            for node in open:
                if node.is_solved():
                    return node
                
                self.explored_states += 1
                
                neighbours = node.get_neighbours()
                for neighbour in neighbours:
                    if neighbour in visited:
                        continue

                    neighbour.h = self.heuristic(neighbour)
                    visited.add(neighbour)
                    successors.append(neighbour)

            successors = sorted(successors, key=lambda x: x.h)
            open = successors[:self.beam_width]


    def solve(self):
        self.explored_states = 0

        h = self.heuristic(self.start_node)
        self.start_node.h = h

        self.final_node = self.beam_search(self.start_node)
        if self.final_node:
            return self.final_node.map, self.explored_states, self.final_node.map.undo_moves
        else:
            return None, self.explored_states, math.inf
    