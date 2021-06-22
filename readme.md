# [LeetCode](https://leetcode.com/) Scaffold and Solutions

Here you will find my [LeetCode](https://leetcode.com/) scaffold with the following base structure:

### What Does it Do Exactly?
The Scaffold pulls in the text file of the same name as the python file in the package being ran and inserts it into the standard input stream. You need only set `lines_per_input` to however many lines in the text file you need and for each loop in the scaffold `main` function use the `input()` function to get the next item.

### Pretty Printing Solutions for All Your Corporate Needs /s

In the `main.py` file you can also set the solution to be printed for easier copying of your solution to the site.

### History is Written by the Victors?

Each solution has a readme that is taken straight from the LeetCode page for it. This is for historical purposes around when I solved the problem in case there are any changes.

### Shut Up and Take my Code!

![img.png](img.png)

```python
class LeetCodeScaffold:
    input_count = 0

    def printe(self, e):
        print(f"{e}", file=sys.stderr)

    def printd(self, d):
        logging.debug(f'{d}')

    def __init__(self, input_file: pathlib.Path):
        if not input_file:
            raise Exception(f"Must supply input file to stdin!")

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

        self.input_file = f"{input_file.parent}{os.sep}{input_file.stem}.txt"
        print(f"Piping {self.input_file} into stdin...")
        self.input_count = len(open(self.input_file, 'r').readlines())
        sys.stdin = io.StringIO(open(self.input_file, 'r').read())
```

An example of a solution:

```python
"""
NumberOfSubarraysWithBoundedMaximum - https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
"""
from typing import List
from Scaffold import ScaffoldClass
import pathlib
import ast


class Solution(ScaffoldClass.LeetCodeScaffold):
    def __init__(self):
        super().__init__(pathlib.Path(__file__))

    def main(self) -> List:
        solutions = []
        lines_per_input = 3  # @TODO: Set this to the number of lines that are in the input
        for solution in range(int(self.input_count / lines_per_input)):
            print(f'\nSolving solution {solution}')
            solutions += [self.numSubarrayBoundedMax(*[ast.literal_eval(input()) for _ in range(lines_per_input)])]
        return solutions

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        self.printd(f'{nums = }, {left = }, {right = }')
        return -1

```
