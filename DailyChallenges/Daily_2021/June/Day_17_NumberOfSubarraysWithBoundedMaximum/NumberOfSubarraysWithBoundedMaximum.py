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
        lines_per_input = 3
        for solution in range(int(self.input_count / lines_per_input)):
            print(f'\nSolving solution {solution}\n{"-" * 100}')
            solutions += [self.numSubarrayBoundedMax(*[ast.literal_eval(input()) for _ in range(lines_per_input)])]
            print(f'{"-" * 100}')
        return solutions

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        self.printd(f'{nums = }, {left = }, {right = }')
        return -1
