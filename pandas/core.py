from io import StringIO
import pandas as pd

def read_text(data, *args, **kwargs):
	return pd.read_csv(StringIO(data), *args, **kwargs)
