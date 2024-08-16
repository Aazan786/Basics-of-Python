from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is Already opened")
        self.opened = True

    def close(self):
        if not self.closed:
            raise InvalidOperationError("Stream is Already opened")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from File")
    
class NetorkStream(Stream):
    def read(self):
        print("Reading data from network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory stream")


    