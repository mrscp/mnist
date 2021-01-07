class Settings(dict):
    """
    This class is for containing all of the settings for the project. This class is a child class of dictionary

    Attributes
    ----------
    self: dict
        Contains settings as a key/value pairs
    """
    def __init__(self):
        super().__init__()
        self["env"] = "local"
        self["mode"] = ["train", "test"]
