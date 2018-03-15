import pandas as pd
import numpy as np
import csv


class Loader(object):
    @classmethod
    def load_csv(cls, filename):
        raw = open(filename, 'rt')
        reader = csv.reader(raw, delimiter=',', quoting=csv.QUOTE_NONE)
        data = np.array(list(reader))
        return data, data.shape
