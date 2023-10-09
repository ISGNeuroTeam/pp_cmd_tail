"""Module for getting a tail of a DataFrame"""
import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax

DEFAULT_NUMBER = 10


class TailCommand(BaseCommand):
    """Class for getting a tail of a DataFrame"""
    # define syntax of your command here
    syntax = Syntax(
        [
            Positional("n", required=False, otl_type=OTLType.INTEGER),
            Keyword("limit", required=False, otl_type=OTLType.INTEGER),
        ],
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # get and check args
        number = self.get_arg("n").value
        if not_none(number) and number <= 0:
            """
            "tail -1" or "tail 0" return no dataframe and error
            """
            print(f"number parameter must have a positive [>=0] integer value, not {number}")
            return pd.DataFrame()
        limit = self.get_arg("limit").value
        if not_none(limit) and limit <= 0:
            print(f"limit parameter must have a positive [>=0] integer value, not {number}")
            return pd.DataFrame()

        elements: int = number if not_none(number) else (limit if not_none(limit) else DEFAULT_NUMBER)
        print(f'{number=} | {limit=} | {elements=}')

        return df.tail(elements)


def not_none(number: int) -> bool:
    return number is not None
