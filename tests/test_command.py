"""Module for testing tail command"""
import os
from unittest import TestCase

import pandas as pd
from postprocessing_sdk.commands.pp import Command
from pytest import raises
from otlang.exceptions import OTLException

# sample dict
DATA = {'a': [2145, 654372, 46, 35678, 865476, 435378, 8647, -418084, -844815, -1271546],
        'b': [1, 2, 3, 4, 5, 6, 7, 42367, 2, 3]}

INDEXES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestCommand(TestCase):
    """Class for testing tail command"""

    def setUp(self):
        self.command = Command()
        commands_dir = '/home/mashida/dev/pp/pp_cmd_tail/venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd'
        self.command._create_command_executor(storage='', commands_dir=commands_dir)
        parent_dir = os.path.dirname(os.getcwd())
        # add current command to self.command with _import_user_commands()
        self.command.command_executor.command_classes.update(
            self.command.command_executor._import_user_commands(commands_directory=parent_dir, follow_links=True))

    def test_supporting_readfile_command(self):
        sample = pd.DataFrame(data=DATA, index=INDEXES)
        # calc
        otl_query_readfile_only = '| readFile example_002.csv type=csv storage=pp_storage '
        result = self.command.run_otl(otl_query=otl_query_readfile_only, storage='')
        # check
        pd.testing.assert_frame_equal(sample, result)

    def run_test_with_otl_query_loop(self, otl: str, n: int) -> None:
        """
        n       4 5 6 7 | 10
        start   6 5 4 3 |
        start = len() - n
        """
        n = len(DATA['a']) if n < 0 else n
        start = len(DATA['a']) - n if len(DATA['a']) - n > 0 else 0
        data2 = {'a': DATA['a'][start:], 'b': DATA['b'][start:]}
        sample = pd.DataFrame(data=data2, index=INDEXES[start:])
        # run tested command
        result = self.command.run_otl(otl_query=otl, storage='', raise_error=True, df_print=False)
        # check
        pd.testing.assert_frame_equal(sample, result)

    def run_failing_test_with_otl_query_loop(self, otl: str) -> None:
        sample = pd.DataFrame()
        # run tested command
        result = self.command.run_otl(otl_query=otl, storage='', raise_error=True, df_print=False)
        # check
        pd.testing.assert_frame_equal(sample, result)

    def test_command_with_both_params(self):
        for i in range(1, 12):
            for j in range(1, 12):
                otl_query = f"| readFile example_002.csv type=csv" \
                            f" storage=pp_storage | tail {i} limit={j}"
                self.run_test_with_otl_query_loop(otl=otl_query, n=i)

    def test_command_with_both_zero_or_negative_params(self):
        for i in range(-3, 1):
            for j in range(-3, 1):
                otl_query = f"| readFile example_002.csv type=csv" \
                            f" storage=pp_storage | tail {i} limit={j}"
                with raises(ValueError):
                    self.run_failing_test_with_otl_query_loop(otl=otl_query)

    def test_command_with_tail_param(self):
        for n in range(1, 12):
            otl_query = f'| readFile example_002.csv type=csv storage=pp_storage | tail {n}'
            self.run_test_with_otl_query_loop(otl=otl_query, n=n)

    def test_command_with_zero_or_negative_tail_param(self):
        for n in range(-3, 1):
            otl_query = f'| readFile example_002.csv type=csv storage=pp_storage | tail {n}'
            with raises(ValueError):
                self.run_failing_test_with_otl_query_loop(otl=otl_query)

    def test_command_with_limit_param(self):
        for n in range(1, 12):
            otl_query = f'| readFile example_002.csv type=csv storage=pp_storage | tail limit={n}'
            self.run_test_with_otl_query_loop(otl=otl_query, n=n)

    def test_command_with_zero_or_negative_limit_param(self):
        for n in range(-3, 1):
            otl_query = f'| readFile example_002.csv type=csv storage=pp_storage | tail limit={n}'
            with raises(ValueError):
                self.run_failing_test_with_otl_query_loop(otl=otl_query)

    def test_no_tail_command(self):
        otl_query: str = f'| readFile example_002.csv type=csv storage=pp_storage | limit=2'
        with raises(OTLException):
            self.run_failing_test_with_otl_query_loop(otl=otl_query)
