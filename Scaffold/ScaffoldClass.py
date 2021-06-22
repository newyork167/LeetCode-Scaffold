import sys
import io
import pathlib
import logging


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

        self.input_file = f"{input_file.parent}/{input_file.stem}.txt"
        print(f"Piping {self.input_file} into stdin...")
        self.input_count = len(open(self.input_file, 'r').readlines())
        sys.stdin = io.StringIO(open(self.input_file, 'r').read())
