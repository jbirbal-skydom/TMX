import serial
import codecs
from conf import Conf
args = Conf("setting\config.jsonc")

ser = serial.Serial(
    port = args["readPort"], 
    baudrate=args["rate"],
    parity=args["Parity"],
    stopbits=args["stopbits"],
    bytesize=args["bytes"], 
     timeout=args["timeout"], 
    )

print (ser.name)        
while True:
    if(ser.in_waiting > 0):
        res = ser.readline()
        # if res == "T":
        #     print ("start")
        #     ser.write("T".encode())
        print(res)
        #ser.write(b"Thank you for sending data \r\n")
