import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax

DEFAULT_NUMBER = 10


class TailCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Positional("n", required=False, otl_type=OTLType.INTEGER),
            Keyword("limit", required=False, otl_type=OTLType.INTEGER),
        ],
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        number = self.get_arg('n').value
        limit = self.get_arg('limit').value
        return df.tail(number or limit or DEFAULT_NUMBER)
