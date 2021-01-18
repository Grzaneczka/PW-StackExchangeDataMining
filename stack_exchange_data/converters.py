""" Custom data converters meant for converting whole data frame column. """
import pandas as pd


def string_to_bool(column: pd.Series) -> pd.Series:
    """ Converts "True" / "False" strings to booleans. Other values are set to NaN. """
    return column.map({'False': False, 'True': True})


def to_numeric(column: pd.Series) -> pd.Series:
    """ Converts to numeric and replaces missing values to NA. """
    return pd.to_numeric(column, errors='coerce')
