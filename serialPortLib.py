import os


class SerialPortState:
    port = None
    state = None
    
    def __init__(self, port, state):
        self.port = port
        self.state = state
    
    def __repr__(self):
        return "%s (%s)" % (self.port, self.state)
        
    def __str__(self):
        return "%s (%s)" % (self.port, self.state)


class SerialPort:
    __port = None
    __baudRate = None
    __serial = None
    __isOpened = False
    
    def __init__(self, port = None, baudRate = None):
        self.__port = port
        self.__baudRate = baudRate
    
    def init(self):
        os.system("@mode %s BAUD=%s" % (self.__port, self.__baudRate))

    def open(self):
        if not self.__isOpened:
            self.__serial = os.open(self.__port, os.O_RDWR)
            self.__isOpened = True
    
    def close(self):
        if self.__isOpened:
            os.close(self.__serial)
            self.__isOpened = False
    
    def setPort(self, port):
        self.__port = port
    
    def setBaudRate(self, baudRate):
        self.__baudRate = baudRate
    
    def isOpened(self):
        return self.__isOpened

    def sendString(self, text):
        os.write(self.__serial, text)
    
    @staticmethod
    def getPorts(count = 10):
        portsList = []
        
        for i in range(1, count + 1):
            try:
                __port = os.open("COM%s" % (i), os.O_RDWR)
                os.close(__port)
            except OSError as e:
                if e.errno == 13: # PermissionError
                    portsList.append(SerialPortState("COM%s" % (i), "busy"))
            except:
                continue
            else:
                portsList.append(SerialPortState("COM%s" % (i), "available"))
        
        return portsList
