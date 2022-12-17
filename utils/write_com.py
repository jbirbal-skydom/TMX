import binascii
import serial
from conf import Conf
import threading
args = Conf("setting\config.jsonc")

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(    
    port = args["writePort"] , 
    baudrate=args["rate"],
    parity=args["Parity"],
    stopbits=args["stopbits"],
    bytesize=args["bytes"], 
    timeout=args["timeout"]
    )
ser.isOpen()
scale = 16

def string2hex(mes):
    res = bytearray.fromhex(mes)
    # res = "0x" + mes
    # res = int(res, 16) #decimal
    # res = hex(res) #Hex


    print (res)
    return res


def pulse():
    t = threading.Timer(0.4, pulse)
    t.start()
    wake = bytearray.fromhex("c0")
    #res = bin(int(wake, scale)).zfill(8)
    ser.write(wake)


#t = threading.Timer(0.4, pulse)
#t.start() 

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')
print (ser.name)  
time = 0
message= 2
encoded = bytearray()
while 1 :

    # get keyboard input
    message = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if message == 'exit':
        ser.close()
        exit()
    if message == 'T':
        ser.write(message.encode())
    if message == 'clear':
        encoded = bytearray()
    if message == 'send':
        print (encoded)
        ser.write(encoded)
        encoded = bytearray()
    else:
        encoded += string2hex(message)

        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        #ser.write(encoded)
        out = ''
        if out != '':
            print (">>" + out)