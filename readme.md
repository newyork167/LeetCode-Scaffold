# [LeetCode](https://leetcode.com/) Scaffold and Solutions

Here you will find my [LeetCode](https://leetcode.com/) scaffold. It will hold up your code in times of uncertainty, and it will most certainly drag it down at any other moment... So be weary and have fun with LeetCode in the comfort of your own IDE instead of theirs!

### What Does it Do Exactly?
The Scaffold pulls in the text file of the same name as the python file in the package being ran and inserts it into the standard input stream. You need only set `lines_per_input` to however many lines in the text file you need and for each loop in the scaffold `main` function use the `input()` function to get the next item.

### Pretty Printing Solutions for All Your Corporate Needs

In the `main.py` file you can also set the solution to be printed for easier copying of your solution to the site.

### History is Written by the Victors?

It is usually a good idea to keep documentation of the page itself so that if LeetCode decides to change anything you aren't left scratching your head as to why nothing works anymore. I have included an example from one of the daily challenges. When the code is less terrible, I will post up my directory staging code. Until then, it would be wise to grab that information on your own!

![img.png](img.png)

The following is the structure in case you would rather look at it in an eye watering readme format instead of clicking through the repo...well here it is!

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

# License

Basically, you do you! Write all the code, learn all the LeetCode skills, and go be a great engineer of the software variety!(?)

### MIT License

Copyright (c) 2021 **Cody Dietz / Newyork167**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
