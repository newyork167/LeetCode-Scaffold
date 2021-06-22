import importlib
import os
from Utilities.Timing import timing
from datetime import datetime

# Stage up details of solution to run - This uses today's date
solve_me_year = datetime.today().year
solve_me_month = f'{datetime.today():%B}'
solve_me_day = datetime.today().day

# To test a particular solution such as the included example
solve_me_year = 2021
solve_me_month = "June"
solve_me_day = 17

# Set to true to print the copyable solution to the terminal output
print_python_solution = True


def get_file_to_solve() -> str:
    global solve_me_day, solve_me_month
    solve_me = f'DailyChallenges.Daily_{solve_me_year}.{solve_me_month}'
    challenges_dir = solve_me.replace('.', os.sep)

    for day_folder in os.listdir(challenges_dir):
        if f"Day_{solve_me_day}" in day_folder:
            solution_files = [x for x in os.listdir(f'{challenges_dir}/{day_folder}') if x.endswith('.py') and x != '__init__.py']
            if not len(solution_files):
                raise Exception(f"Cannot find solution in {challenges_dir}/{day_folder}")
            solve_me += f'.{day_folder}.{solution_files[0].split(".py")[0]}'
            break

    return solve_me


def print_leetcode_solution(solution_file):
    import inspect
    in_user_def_func = False

    print(f"{'-' * 10} COPY BELOW {'-' * 10}\n")

    lines = inspect.getsourcelines(solution_file)[0]
    for line in lines:
        # Cull any non solution space lines and print
        if ('def' in line and not ('__init__' in line or 'def main' in line)) or ('class Solution' in line):
            in_user_def_func = True
        elif 'def ' in line and ('__init__' in line or 'def main' in line):
            in_user_def_func = False

        if in_user_def_func:
            if '(ScaffoldClass.LeetCodeScaffold)' in line:
                line = line.replace('(ScaffoldClass.LeetCodeScaffold)', '')
            print(line.strip('\n'))

    print(f"\n{'-' * 10} COPY ABOVE {'-' * 10}")


@timing
def main():
    solution_file = get_file_to_solve()
    to_solve = importlib.import_module(solution_file)
    solutions = to_solve.Solution().main()
    print(f"\nSolutions: {solutions}\n")

    if print_python_solution:
        print_leetcode_solution(solution_file=to_solve)


if __name__ == '__main__':
    main()
