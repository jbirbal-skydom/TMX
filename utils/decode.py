import serial
import serial.tools.list_ports
import time


#from utils.conf import Conf
#args = Conf("setting//config.json")

statuspair= {
    211:193,
    212:194,
    214:197
}





class com():
    def __init__(self) -> None:
        self.port = None
        self.ser = None

        ports = list(serial.tools.list_ports.comports())
        if self.port == None:
            for p in ports:
                if 'USB Serial Port' in p.description:
                    if p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")] == "0403":
                        print("found")
                        # Connection to port

                        a = p.hwid
                        b = p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")]
                        self.port = (p.device)
                        self.connect(self.port)
                        break
                self.port = None #args["writePort"]
            

    def connect(self, p):

        if self.port != None:
            self.ser.close()
        self.port = p

        # configure the serial connections (the parameters differs on the device you are connecting to)
        try: 
            self.ser = serial.Serial(    
                port = self.port, 
                baudrate=4800, #args["rate"],
                parity= "N", #args["Parity"],
                stopbits= 1, #args["stopbits"],
                bytesize= 8, #args["bytes"], 
                timeout= 1 #args["timeout"]
            )
            self.ser.isOpen()
            self.time = 1
        except serial.SerialException as e:
            print ("not connected", e)
            self.ser = None
            self.port = None


    def isConnected(self):
        '''Is the computer connected with the MS-2000?'''
        try:
            return self.ser.isOpen()
        except:
            return False

    def pulse(self):
        # t = threading.Timer(self.time, self.pulse)
        # t.start()
        wake = bytearray.fromhex("c0")
        self.ser.write(wake)


    def request_data(self, info):
        for k in info.keys():
            self.ser.reset_input_buffer()
            replied = 0
            self.ser.write (k.to_bytes(1,byteorder='big'))
            if k == 192:
                expected = 2
            elif k == 200 or k == 201:
                expected = 3
            else: 
                expected = 5          
            while replied == 0:
                if (self.ser.in_waiting > 0):
                   info[k] = self.ser.read(expected)
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
            reqd = min(reqd, 100)
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
                res = self.ser.read(5)
                replied = 1
        return res
        
        








