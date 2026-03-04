from sokoban.map import Map

class Node():
    def __init__(self, map: Map, h=None, parent=None):
        self.map = map
        self.parent = parent
        self.h = h

    def is_solved(self):
        return self.map.is_solved()
    
    def get_neighbours(self):
        reachable_positions = self.map.get_reachable_positions()

        neighbours = []

        for pos in reachable_positions:
            if not self.map.is_near_box(pos):
                continue
            state = self.map.copy()
            state.player.x, state.player.y = pos
            neighs = state.get_neighbours(box_moves_only=True)
            neighs = [Node(neigh, parent=Node(state, h=self.h, parent=self)) for neigh in neighs]
            neighbours.extend(neighs)

        return neighbours
    
    def __hash__(self):
        return hash(str(self.map))

    def __eq__(self, other):
        return isinstance(other, Node) and str(self.map) == str(other.map)