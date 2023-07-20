import subprocess
from unittest import TestCase
from pandas import DataFrame

# /home/svyatoslav/PycharmProjects/postprocessing_test_1/venv/bin/pp
TEST_STRING = "| readFile example_002.csv type=csv storage=pp_storage | tail 5"
EXPECTED_RESULT = "readFile example_002.csv type=csv storage=pp_storage"


def capture(s):
    x = subprocess.run(['pp', s], capture_output=True).stdout.decode()
    x = [n.split() for n in x[:-1].split('\n')]
    x = [x[0]] + [lst[1:] for lst in x[1:]]
    x = DataFrame(x[1:], columns=x[0])
    return x


class TestCommand(TestCase):

    def test_n(self):
        sample = capture(EXPECTED_RESULT)
        result = capture(TEST_STRING)

        self.assertEqual(sample, result)
