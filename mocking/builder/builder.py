import pandas as pd
from dataclasses import dataclass
from icecream import ic


@dataclass
class Config:
    rows: int
    columns: list[dict]


# For col in dict -> Col def = define(col)
# Col def takes the type, and other specifications
# Then has a method for generating n rows of that type, given a specification
class Builder:
    def __init__(self) -> None:
        pass

    def parse_config(self, config: dict) -> None:
        self.config = Config(**config)

    def make_df(self) -> pd.DataFrame:
        col_list = [next(iter(c.keys())) for c in self.config.columns]
        index = range(self.config.rows)
        df = pd.DataFrame(columns=col_list, index=index)
        return df
