""" Functions for loading the Stack Exchange data. """
import glob
import tempfile
import urllib.request
import os
import warnings
from typing import List, Union
from xml.etree import ElementTree

import py7zr
import pandas as pd
from tqdm.auto import tqdm

from stack_exchange_data import StackExchangeData
from stack_exchange_data.data_format import STACK_EXCHANGE_DATA_FORMATS


def load_from_url(urls: Union[str, List[str]]) -> StackExchangeData:
    """ Downloads and loads StackExchange data from url(s). """
    if not isinstance(urls, list):
        urls = [urls]

    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = [os.path.join(temp_dir, f'data{i}.7z') for i in range(len(urls))]

        for path, url in tqdm(list(zip(file_paths, urls)), desc='Downloading'):
            urllib.request.urlretrieve(url, path)

        return load_from_archive(file_paths)


def load_from_archive(paths: Union[str, List[str]]) -> StackExchangeData:
    """ Loads StackExchange data from 7z archive(s). """
    if not isinstance(paths, list):
        paths = [paths]

    with tempfile.TemporaryDirectory() as temp_dir:
        for path in tqdm(paths, desc='Extracting'):
            py7zr.SevenZipFile(path, mode='r').extractall(temp_dir)

        return load_from_path(temp_dir)


def load_from_path(path: str) -> StackExchangeData:
    """ Loads StackExchange data from path. """
    data = {}

    # load each XML file
    for file_path in tqdm(glob.glob(os.path.join(path, '*.xml')), desc='Loading'):
        tree = ElementTree.parse(file_path)
        root = tree.getroot()

        # check which data it is based on the root tag
        if root.tag not in STACK_EXCHANGE_DATA_FORMATS:
            warnings.warn(f'Unknown root tag "{root.tag}" encountered in {file_path}')
            continue

        # load rows
        df = pd.DataFrame(
            (row.attrib for row in root.findall('row'))
        )

        # apply converters
        for col, func in STACK_EXCHANGE_DATA_FORMATS[root.tag].get('converters', {}).items():
            df[col] = func(df[col])

        # cast data types
        df = df.astype(STACK_EXCHANGE_DATA_FORMATS[root.tag].get('dtypes', {}))

        data[root.tag] = df

    return StackExchangeData(**data)
