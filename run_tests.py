import os
import sys
import time
import pandas as pd
from sokoban import (Map, gif)
from search_methods.ida_star import IDAStar
from search_methods.beam_search import BeamSearch

TEMP_DIR = "steps"
OUT_DIR = 'out'

tests = [
    'easy_map1',
    'easy_map2',
    'medium_map1',
    'medium_map2',
    'hard_map1',
    'hard_map2',
    'super_hard_map1',
    'large_map1',
    'large_map2'
]


def run_test(solver, create_gif=False, out_file=None):
    start_time = time.time()
    final_state, explored_states, pull_moves = solver.solve()
    elapsed_time = time.time() - start_time

    if final_state:
        print(f"Explored states: {explored_states}")
        print(f"Pull moves: {pull_moves}")
        print(f"Time: {elapsed_time:.02f} s")
        if create_gif and out_file:
            steps = solver.get_path()
            empty_dir(TEMP_DIR)
            gif.save_images(steps, TEMP_DIR)
            gif.create_gif(TEMP_DIR, f"{out_file}.gif", OUT_DIR)
    else:
        print("No solution found.")

    return explored_states, pull_moves, elapsed_time


def run_all_tests(algorithm, pull_cost, beam_width=70, csv_file_name=None, create_gifs=False, skip=[]):
    if algorithm == 'ida_star':
        print(f'----- IDA*: pull_cost={pull_cost} -----')
    elif algorithm == 'beam_search':
        print(f'----- Beam Search: pull_cost={pull_cost}, beam_width={beam_width} -----')
    else:
        return

    results = []

    for i in range(len(tests)):
        if i in skip:
            continue
        print(tests[i])
        test_file = f"tests/yaml/{tests[i]}.yaml"
        map = Map.from_yaml(test_file)
        if algorithm == 'ida_star':
            solver = IDAStar(map, pull_cost)
        else:
            solver = BeamSearch(map, pull_cost, beam_width)
        
        explored_states, pull_moves, elapsed_time = run_test(solver, create_gif=create_gifs, out_file=tests[i])
        
        results.append({
            "Test": tests[i],
            "Algorithm": algorithm,
            "Explored States": explored_states,
            "Pull Moves": pull_moves,
            "Time (s)": elapsed_time
        })
        
        print('\n')

    print('\n')

    if csv_file_name and results:
        df = pd.DataFrame(results)
        df.to_csv(csv_file_name, index=False)
        print("Saved results to CSV.")


def empty_dir(dir):
    if os.path.exists(dir):
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)


def solve(solver, result):
    result.append(solver.solve())


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 run_tests.py <test_number> [gifs=yes/no] [csv=yes/no]')
        sys.exit(1)

    test = int(sys.argv[1])

    create_gifs = False
    create_csv = False
    
    if len(sys.argv) >= 2:
        for arg in sys.argv[2:]:
            k, v = arg.split('=')
            if k == 'gifs' and v == 'yes':
                create_gifs = True
            elif k == 'csv' and v == 'yes':
                create_csv = True

    if test == 1:
        run_all_tests('beam_search', pull_cost=10, beam_width=10, create_gifs=create_gifs,
                      csv_file_name='beam_search_10_10.csv' if create_csv else None)
    elif test == 2:
        run_all_tests('beam_search', pull_cost=10, beam_width=70, create_gifs=create_gifs,
                      csv_file_name='beam_search_10_70.csv' if create_csv else None)
    elif test == 3:
        run_all_tests('ida_star', pull_cost=1.5, create_gifs=create_gifs,
                      csv_file_name='ida_star_1_5.csv' if create_csv else None)
    elif test == 4:
        run_all_tests('ida_star', pull_cost=10, skip=[6,8], create_gifs=create_gifs,
                      csv_file_name='ida_star_10.csv' if create_csv else None)
    

if __name__ == '__main__':
    main()
