from sokoban.map import Map
from search_methods.node import Node
from collections import deque
import math


class Solver:
    def __init__(self, map: Map, pull_cost : float = 10) -> None:
        self.start_node = Node(map)
        self.final_node = None
        self.pull_cost = pull_cost
        self.explored_states = 0
        self.dist_map = [[]]

    def solve(self):
        raise NotImplementedError
    
    def bfs_target_dist(self, map, target):
        visited = set()
        queue = deque([(target, 0)])

        while queue:
            (x, y), dist = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            self.dist_map[x][y][target] = dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if map.is_valid_position((nx, ny)):
                    queue.append(((nx, ny), dist + 1))

    def compute_goal_dist(self, map):
        for target in map.targets:
            self.bfs_target_dist(map, target)

        for x in range(map.length):
            for y in range(map.width):
                if (x, y) in map.targets:
                    self.dist_map[x][y] = 0
                elif (x, y) in map.obstacles or self.dist_map[x][y] == {}:
                    self.dist_map[x][y] = math.inf

    def heuristic(self, node: Node) -> float:
        state = node.map
        h = 0

        for box_x, box_y in state.positions_of_boxes:
            dist = self.dist_map[box_x][box_y]

            if dist == math.inf:
                return math.inf
            elif dist == 0:
                continue
 
            dists = []
            for target in state.targets:
                if target not in state.positions_of_boxes:
                    dists.append(self.dist_map[box_x][box_y][target])

            h += sum(dists) / len(dists)

            reachable_positions = state.get_reachable_positions(ignore_boxes=True)
            
            if not state.can_push_box((box_x, box_y), reachable_positions):
                h += self.pull_cost - 1

        return h
    
    def bfs_player_path(self, map, start, end):
        visited = set()
        queue = deque([(start, [])])

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path[:-1]

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if map.is_valid_position((nx, ny)) and not (nx, ny) in map.positions_of_boxes:
                    queue.append(((nx, ny), path + [(nx, ny)]))

        return []
    
    def get_path(self):
        node = self.final_node
        path = []

        maps = []
        while node:
            maps.append(node.map)
            node = node.parent
        maps = maps[::-1]

        for i in range(len(maps) - 1):
            current_map = maps[i]
            next_map = maps[i + 1]

            current_pos = (current_map.player.x, current_map.player.y)
            next_pos = (next_map.player.x, next_map.player.y)

            if current_pos == next_pos:
                continue

            player_path = self.bfs_player_path(current_map, current_pos, next_pos)

            for (pos_x, pos_y) in player_path:
                new_map = current_map.copy()
                new_map.player.x = pos_x
                new_map.player.y = pos_y
                path.append(new_map)

            path.append(next_map)

        return path
