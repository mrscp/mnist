import yaml
from os.path import join
import os
import sys
from lib.settings import Settings


class Config(Settings):
    """
    This class is used to represent whole configuration of the project. Reads the config.*.yml file and assigns the
    variables as key/value pairs
    Attributes
    ----------
    environment: str
        variable for which environment should be loaded
    project_dir
        Project path
    _config_location
        config file location
    """
    def __init__(self, project_dir=None):
        super().__init__()
        self.environment = "local"
        if project_dir is not None:
            self.project_dir = join("/", *project_dir.split("/"))
        else:
            self.project_dir = os.path.dirname(sys.modules['__main__'].__file__)

        self._config_location = join(self.project_dir, "config.{}.yaml".format(self.environment.lower()))

        self._load_config(self._config_location)

    def _load_config(self, config_location):
        try:
            with open(config_location, 'r') as stream:
                try:
                    self.update(yaml.safe_load(stream))
                except yaml.YAMLError as exc:
                    raise exc
        except FileNotFoundError:
            self._load_config(join(self.project_dir, "config.{}.yml".format(self.environment.lower())))
