import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class TailCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Positional("n", required=False, otl_type=OTLType.INTEGER),
            Keyword("limit", required=False, otl_type=OTLType.INTEGER),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start tail command')
        # getting arguments values
        n = self.get_arg("n").value
        limit = self.get_arg("limit").value
        self.log_progress(f'Input arguments: {n=} | {limit=}')

        # Checking if arguments exist
        if n is None and limit is None:
            raise ValueError('No "n" or "limit" arguments given')

        # calculating
        n = n or limit

        return df[-n:]
