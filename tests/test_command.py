"""Module for testing tail command"""
import subprocess
from unittest import TestCase

SAMPLE = [["aa", "b", "c"],
          ["3", "AAA", "10001"],
          ["3", "DDD", "10002"],
          ["1", "EEE", "1000001"],
          ["4", "CCC", "3"],
          ["3", "BBB", "15"]]


def capture(s):
    """Captures the output of postprocessing
     command s and turns it into a list"""
    x = subprocess.run(["pp", s],
                       check=False,
                       capture_output=True).stdout.decode()
    x = [n.split() for n in x[:-1].split("\n")]
    x = [x[0]] + [lst[1:] for lst in x[1:]]
    return x


class TestCommand(TestCase):
    """Class for testing tail command"""

    # Testing N
    def test_n(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv " \
                          f"storage=pp_storage | tail {i}"
            sample = SAMPLE[len(SAMPLE) - i:]
            sample.reverse()
            sample = [SAMPLE[0]] + sample
            result = capture(test_string)
            self.assertEqual(sample, result)

    # Testing limit
    def test_limit(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv" \
                          f" storage=pp_storage | tail limit={i}"
            sample = SAMPLE[len(SAMPLE) - i:]
            sample.reverse()
            sample = [SAMPLE[0]] + sample
            result = capture(test_string)
            self.assertEqual(sample, result)

    # Testing both of them. In this case, n is prioritized over limit
    def test_both(self):
        for i in range(2, 6):
            for j in range(2, 6):
                test_string = f"| readFile example_002.csv type=csv" \
                              f" storage=pp_storage | tail {i} limit={j}"
                sample = SAMPLE[len(SAMPLE) - i:]
                sample.reverse()
                sample = [SAMPLE[0]] + sample
                result = capture(test_string)
                self.assertEqual(sample, result)

    # all the same tests, but compared with wrong answers
    def test_bad_n(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv " \
                          f"storage=pp_storage | tail {i}"
            sample = SAMPLE[len(SAMPLE) - i + 1:]
            sample.reverse()
            sample = [SAMPLE[0]] + sample
            sample1 = SAMPLE[len(SAMPLE) - i - 1:]
            sample1.reverse()
            sample1 = [SAMPLE[0]] + sample1
            result = capture(test_string)
            self.assertNotEqual(sample, result)
            self.assertNotEqual(sample1, result)

    def test_bad_l(self):
        for i in range(2, 6):
            test_string = f"| readFile example_002.csv type=csv " \
                          f"storage=pp_storage | tail limit={i}"
            sample = SAMPLE[len(SAMPLE) - i + 1:]
            sample.reverse()
            sample = [SAMPLE[0]] + sample
            sample1 = SAMPLE[len(SAMPLE) - i - 1:]
            sample1.reverse()
            sample1 = [SAMPLE[0]] + sample1
            result = capture(test_string)
            self.assertNotEqual(sample, result)
            self.assertNotEqual(sample1, result)

    def test_bad_both(self):
        for i in range(2, 6):
            for j in range(2, 6):
                test_string = f"| readFile example_002.csv type=csv " \
                              f"storage=pp_storage | tail {i} limit={j}"
                sample = SAMPLE[len(SAMPLE) - i + 1:]
                sample.reverse()
                sample = [SAMPLE[0]] + sample
                sample1 = SAMPLE[len(SAMPLE) - i - 1:]
                sample1.reverse()
                sample1 = [SAMPLE[0]] + sample1
                result = capture(test_string)
                self.assertNotEqual(sample, result)
                self.assertNotEqual(sample1, result)
