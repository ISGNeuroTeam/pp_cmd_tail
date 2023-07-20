import re
import subprocess
from unittest import TestCase
from pandas import DataFrame

# /home/svyatoslav/PycharmProjects/postprocessing_test_1/venv/bin/pp
TEST_STRING = "| readFile example_002.csv type=csv storage=pp_storage | tail 5"
EXPECTED_RESULT = "readFile example_002.csv type=csv storage=pp_storage"


def get_df():
    print('a')


class TestCommand(TestCase):

    # нужно протестировать
    # n
    def test_n(self):
        sample = subprocess.run(['pp', EXPECTED_RESULT], capture_output=True).stdout.decode()
        sample = [x.split() for x in sample[:-1].split('\n')]
        sample = [sample[0]]+[lst[1:] for lst in sample[1:]]
        result = subprocess.run(['pp', TEST_STRING], capture_output=True).stdout.decode()
        result = [x.split() for x in result[:-1].split('\n')]
        result = [result[0]] + [lst[1:] for lst in result[1:]]
        df = DataFrame(result[1:], columns=result[0])

        self.assertEqual(sample, df)
    #
    #
    #
    #
