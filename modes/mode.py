from lib.config import Config
from time import time
from datetime import timedelta
from os.path import join


class Mode(Config):
    """
    Mode class is a abstract class for all other modes, basically this class holds the common attributes and methods
    for the modes

    Attributes
    ----------
    _start_time: time
        Start time of the execution

    Methods
    -------
    status(self)
        Default status of the class execution time

    __del__(self)
        Destructor for the class, it automatically starts executing when work of the class is completed
    """
    def __init__(self):
        super(Mode, self).__init__()
        self._start_time = time()

    @staticmethod
    def get_value(param, default_value):
        """
        Get the param value, if param is None then return default value
        :param param: Original value
        :param default_value: Default value for the parameter
        :return: selected value
        """
        return param if param is not None else default_value

    def get_data_location(self, location):
        return join(self["main"]["data_root"], location)

    def status(self):
        """
        Status to be printed when the execution completes
        :return: Default status, Default status is execution time
        """
        return "\n\nExecution time[{}]: {}".format(self.__class__.__name__, timedelta(seconds=time() - self._start_time))

    def __del__(self):
        """
        Destructor for the mode/mode child classes
        :return: None
        """
        print(self.status())
