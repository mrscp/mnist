import pandas as pd


class Dataset:
    def __init__(self, location):
        self._dataset = pd.read_csv(location)
        self._x_cols = self._dataset.columns[1:]
        self._y_cols = self._dataset.columns[:1]

    def generator(self, batch_size=32):
        while True:
            batch = self._dataset.sample(batch_size)

            x = batch[self._x_cols].values.reshape((-1, 28, 28, 1))  # .reshape((-1, 784, 1))
            y = batch[self._y_cols].values
            yield x, y
