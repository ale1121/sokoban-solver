import os
import sys
import time
import threading
from sokoban import (Map, gif)
from search_methods.ida_star import IDAStar
from search_methods.beam_search import BeamSearch
import run_tests


TEMP_DIR = "steps"
OUT_DIR = 'images'


def empty_dir(dir):
    if os.path.exists(dir):
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <algorithm> <test_file> [pull cost] [beam width]")
        sys.exit(1)

    algorithm = sys.argv[1]
    test_file = sys.argv[2]
    pull_cost = None if len(sys.argv) < 4 else float(sys.argv[3])
    beam_width = None if len(sys.argv) < 5 else int(sys.argv[4])

    empty_dir(TEMP_DIR)

    map = Map.from_yaml(test_file)

    solver = None

    if algorithm == 'ida_star':
        pull_cost = pull_cost if pull_cost else 1.5
        solver = IDAStar(map, pull_cost=pull_cost)
        print(f"--- IDA*: pull_cost={pull_cost} ---")
    elif algorithm == 'beam_search':
        pull_cost = pull_cost if pull_cost else 10
        beam_width = beam_width if beam_width else 70
        solver = BeamSearch(map, pull_cost=pull_cost, beam_width=beam_width)
        print(f"--- Beam Search: pull_cost={pull_cost}, beam_width={beam_width} ---")
    if not solver:
        print(f"Algorithm {algorithm} is not ida_star or beam_search")
        sys.exit(1)

    run_tests.run_test(solver, create_gif=True, out_file='solution')

if __name__ == '__main__':
    main()
