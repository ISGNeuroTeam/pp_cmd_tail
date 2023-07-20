import subprocess
from unittest import TestCase
from pandas import DataFrame

SAMPLE = [['aa', 'b', 'c'], ['3', 'AAA', '10001'], ['3', 'DDD', '10002'], ['1', 'EEE', '1000001'], ['4', 'CCC', '3'], ['3', 'BBB', '15']]


def capture(s):
    """Captures the output of postprocessing command s and turns it into a Dataframe"""
    x = subprocess.run(['pp', s], capture_output=True).stdout.decode()
    x = [n.split() for n in x[:-1].split('\n')]
    x = [x[0]] + [lst[1:] for lst in x[1:]]
    return x


class TestCommand(TestCase):
    # Testing N
    def test_n(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv storage=pp_storage | tail {i}"
            sample = [SAMPLE[0]]+SAMPLE[len(SAMPLE)-i:]
            result = capture(test_string)
            self.assertEqual(sample, result)

    # Testing limit
    def test_limit(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv storage=pp_storage | tail limit={i}"
            sample = [SAMPLE[0]]+SAMPLE[len(SAMPLE)-i:]
            result = capture(test_string)
            self.assertEqual(sample, result)

    def test_both(self):
        for i in range(2, 6):
            for j in range(2, 6):
                test_string = f"| readFile example_002.csv type=csv storage=pp_storage | tail {i} limit={j}"
                sample = [SAMPLE[0]]+SAMPLE[len(SAMPLE)-i:]
                result = capture(test_string)
                self.assertEqual(sample, result)
