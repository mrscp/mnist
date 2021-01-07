from modes.mode import Mode
from tensorflow import config
from processor.dataset import Dataset

from models.dl import fully_connected
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam

# Setting up GPU memories to be used for the models
if config.list_physical_devices('GPU'):
    print("using GPU")
    physical_devices = config.list_physical_devices('GPU')
    config.experimental.set_memory_growth(physical_devices[0], enable=True)
    config.experimental.set_virtual_device_configuration(
        physical_devices[0],
        [config.experimental.VirtualDeviceConfiguration(memory_limit=4000)]
    )
else:
    print("using CPU")
    config.set_visible_devices([], 'GPU')


class Train(Mode):
    """
    Training class for the AlexNet for classifying solar images.
    """
    def __init__(self):
        super().__init__()
        print("Mode: Train")

        dataset = Dataset(self.get_data_location(self["train"]["dataset"]))
        x, y = next(dataset.generator(8))
        print(x.shape, y.shape)

        model = fully_connected((28, 28, 1), 10)
        optimizer = Adam(0.001)
        model.compile(loss=categorical_crossentropy, optimizer=optimizer, metrics=["accuracy"])
        reduce_lro_n_plat = ReduceLROnPlateau(
            monitor='loss',
            factor=0.8,
            patience=20,
            verbose=1,
            mode='auto',
            min_delta=0.0001,
            cooldown=10,
            min_lr=1e-10
        )
        early = EarlyStopping(monitor="loss", mode="min", patience=20)
        callbacks_list = [early, reduce_lro_n_plat]

        model.fit(
            dataset.generator(batch_size=self["train"]["batch_size"]),
            steps_per_epoch=self["train"]["steps_per_epoch"],
            epochs=self["train"]["epochs"],
            callbacks=callbacks_list
        )

