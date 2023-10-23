import os
import sys

if __name__ == '__main__':
    print("Environment Path: ", os.environ.get('CONDA_PREFIX'))
    print("System Prefix: ", sys.prefix)
