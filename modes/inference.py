from modes.mode import Mode
from processor.dataset import Dataset

from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd


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
        print("Saving submission file...")
        dataset = pd.read_csv(self.get_data_location("dataset/test.csv"))
        dataset = dataset.values.reshape((-1, 28, 28, 1))/255
        y_hat = model.predict(dataset)
        y_hat = np.argmax(y_hat, axis=1)
        image_ids = np.arange(1, len(y_hat)+1)
        dataset = pd.DataFrame({"ImageId": image_ids, "Label": y_hat})
        dataset.to_csv(self.get_data_location("submission.csv"), index=False)
        print("Done")
        # print(y_hat, image_ids)
