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
        # sample = subprocess.run(['pp', EXPECTED_RESULT], capture_output=True).stdout.decode()
        # sample = [x.split() for x in sample.split('\n')]
        # sample = [lst[1:] for lst in sample]
        result = subprocess.run(['pp', TEST_STRING], capture_output=True).stdout.decode()
        result = re.sub('\n[1234567890]* *', '\n', result)[:-1]
        result = [x.split() for x in result.split('\n')]
        df = DataFrame(result[1:], columns=result[0])

        self.assertEqual(sample, result)
    #
    #
    #
    #
