import serial
import threading
from utils.conf import Conf
args = Conf("setting\config.jsonc")

statuspair= {
    211:193,
    212:194,
    214:197
}





class com():
    def __init__(self) -> None:

        # configure the serial connections (the parameters differs on the device you are connecting to)
        self.ser = serial.Serial(    
            port = args["writePort"] , 
            baudrate=args["rate"],
            parity=args["Parity"],
            stopbits=args["stopbits"],
            bytesize=args["bytes"], 
            timeout=args["timeout"]
        )
        self.ser.isOpen()
        self.time = 1
    

    def pulse(self):
        # t = threading.Timer(self.time, self.pulse)
        # t.start()
        wake = bytearray.fromhex("c0")
        self.ser.write(wake)


    def request_data(self, info):
        for k in info.keys():
            self.ser.write (k.to_bytes(1,byteorder='big'))
            replied = 0
            while replied == 0:
                if (self.ser.in_waiting > 0):
                    info[k] = self.ser.readline()
                    replied = 1
       # print (info)

    def info (self, mes):
        
        req = ( int(mes[0])) # req key pair of message
        reqd = ((mes[1:].decode())) #value
        
        if req in statuspair.keys():
            req = ( statuspair[req])
            #print("The key exists")
        else:
            req = 0
            #print("The key doesn't exist")
        info = int(reqd)

        return (req, info)

    def send (self, command: int, raw=None, increment= None, end=None ) -> str:
        ## format message
        enc = bytearray()
        req = command
        enc += req.to_bytes(1,byteorder='big')

        if increment is not None:
            _, curval = self.info(raw) # get set
            reqd = ((curval+increment))  # increment
            reqd = min(reqd, 10)
            reqd = max (0, reqd)
            reqd = str(reqd).zfill(4)  # str of value
            for c in reqd:
                enc += c.encode()
                
        if end is not None:
             enc += end.to_bytes(1,byteorder='big')


        # send message
        self.ser.write(enc)

        #wait for reponse
        replied = 0
        while replied == 0:
            if (self.ser.in_waiting > 0):
                res = self.ser.readline()
                replied = 1
        return res
        
        








