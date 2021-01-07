from modes.mode import Mode
from processor.dataset import Dataset

from tensorflow.keras.models import load_model
import numpy as np


class Inference(Mode):
    def __init__(self):
        super().__init__()
        print("Mode: Inference")

        dataset = Dataset(self.get_data_location(self["train"]["dataset"]))

        x, y = next(dataset.generator())
        model = load_model(self.get_data_location(self["main"]["model_location"], "1"))
        y_hat = model.predict(x)

        y = np.argmax(y, axis=1)
        y_hat = np.argmax(y_hat, axis=1)

        print("Actual Digits:\t\t", y)
        print("Predicted Digits:\t", y_hat)
        print("Accuracy: ", (y == y_hat).mean())
