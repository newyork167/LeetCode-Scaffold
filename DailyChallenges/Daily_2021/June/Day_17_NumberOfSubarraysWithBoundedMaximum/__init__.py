"""
NumberOfSubarraysWithBoundedMaximum
"""
from typing import List
from Scaffold import ScaffoldClass
import pathlib
import ast


class Solution(ScaffoldClass.LeetCodeScaffold):
    def __init__(self):
        super().__init__(pathlib.Path(__file__))

    def main(self):
        solutions = []
        lines_per_input = 1
        for solution in range(int(self.input_count / lines_per_input)):
            print(f'\nSolving solution {solution}')
            solutions += [self.REPLACE_ME(ast.literal_eval(input()))]
        return solutions

    def REPLACE_ME(self):
        pass
