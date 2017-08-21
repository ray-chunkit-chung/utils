
import os
from io import StringIO
import pandas as pd


PWD = os.path.curdir(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(PWD, '..'))
ROOT = os.path.normpath(os.path.join(SRC, '..'))

__all__ = ['read_string']

def read_string(data, *args, **kwargs):
	return pd.read_csv(StringIO(data), *args, **kwargs)
