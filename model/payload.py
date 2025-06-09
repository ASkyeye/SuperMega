import logging

from model import *
from model.defs import *

logger = logging.getLogger("Payload")


class Payload():
    def __init__(self, filepath: FilePath):
        self.payload_path: FilePath = filepath
        self.payload_data: bytes = b""


    def init(self) -> bool:
        logging.info("-( Load payload: {}".format(self.payload_path))
        if not os.path.exists(self.payload_path):
            logger.error("Payload file does not exist: {}".format(self.payload_path))
            return False

        with open(self.payload_path, 'rb') as f:
            self.payload_data = f.read()
        return True

