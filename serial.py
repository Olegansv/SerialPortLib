import os
from subprocess import call

class SerialPort:
    __port = None
    __baudRate = None
    __serial = None
    __logging = True
    __isOpened = False
    
    def __init__(self, port = None, baudRate = None, logging = True):
        self.__port = port
        self.__baudRate = baudRate
        self.__logging = logging
    
    def init(self):
        call(["serial_init.exe", str(self.__port), str(self.__baudRate)])

    def open(self):
        if self.__isOpened:
            raise OSError("Port %s already opened" % (self.__port))
        else:
            self.__serial = os.open(self.__port, os.O_RDWR)
            self.__isOpened = True
            if self.__logging:
                print("Port %s opened" % (self.__port))
    
    def setPort(self, port):
        if not self.__isOpened:
            self.__port__ = port
    
    def setBaudRate(self, baudRate):
        if not self.__isOpened:
            self.__baudRate = baudRate
    
    def isOpened(self):
        return self.__isOpened

    def send(self, text):
        if self.__isOpened:
            os.write(self.__serial, text)
