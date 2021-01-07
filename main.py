from modes.mode import Mode
import argparse

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


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
            print(mode)
        elif mode == "test":
            print(mode)
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
