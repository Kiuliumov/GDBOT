from abc import ABC, abstractmethod
from constants import banned
import logging


class Login(ABC):
    @abstractmethod
    def __init__(self, app_id):
        self.app_id = app_id
        if self.app_id in banned:
            logging.log('There seems to be a problem and some functionality might not work!\n'
                        'Your client ID is either banned or not valid!\n'
                        'Please contact Kiuliumov#9133 on discord for more information!')
