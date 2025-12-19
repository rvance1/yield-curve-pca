import polars as pl
import os
from utils import MATURITIES 

class Table:
    def __init__(self, path: str):
        self.path = path

    def scan(self) -> pl.LazyFrame:
        return pl.scan_parquet(self.path)
    
yields_table_raw = Table(path = os.getenv("YIELDS_TABLE_PATH"))

yields_table = (yields_table_raw.scan().select(
    ["date"] + MATURITIES
)
)

delta_yields_table = (yields_table.unpivot(
    index="date", variable_name="maturity", value_name="yield"
)
.with_columns(
    pl.col("yield").shift(1).over("maturity").alias("lag_yield")
)
.with_columns(
    (pl.col("yield") - pl.col("lag_yield")).alias("delta_yld")
)
.select(
    "date",
    "maturity",
    "delta_yld"
)
)