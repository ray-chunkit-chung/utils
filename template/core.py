
import os

PWD = os.path.curdir(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(PWD, '..'))
ROOT = os.path.normpath(os.path.join(SRC, '..'))

__all__ = ['hello']

def hello():
	print('hello')