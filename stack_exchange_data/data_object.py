import pickle
from typing import NamedTuple

import pandas as pd


class StackExchangeData(NamedTuple):
    """ Tuple that stores all data from one StackExchange website. """
    badges: pd.DataFrame
    comments: pd.DataFrame
    posthistory: pd.DataFrame
    postlinks: pd.DataFrame
    posts: pd.DataFrame
    tags: pd.DataFrame
    users: pd.DataFrame
    votes: pd.DataFrame

    def save(self, file_path: str):
        """ Saves this object as a pickle. """
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, file_path: str) -> 'StackExchangeData':
        """ Loads StackExchangeData object from pickle. """
        with open(file_path, 'rb') as f:
            return pickle.load(f)
