from modes.mode import Mode
import argparse
from tensorflow import config


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

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

from modes.train import Train
from modes.inference import Inference


class Main(Mode):
    """
    This is the main class, every mode of the project will start by executing this class
    """
    def __init__(self):
        super(Main, self).__init__()

        parser = argparse.ArgumentParser("Searching arguments")

        # basic parameter
        parser.add_argument("--mode", help="Mode for the project.", type=str)
        args = parser.parse_args()

        mode = Mode.get_value(args.mode, self["main"]["mode"])

        if mode == "train":
            Train()
        elif mode == "test":
            Inference()
        else:
            print("Wrong mode! Available modes are: ", self["mode"])

    def status(self):
        """
        Status to be printed at the end of the execution. Override method from Mode class.

        :return: Empty string for printing nothing at the end of the execution of this class.
        """
        return ""


if __name__ == '__main__':
    Main()
