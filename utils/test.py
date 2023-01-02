import random
import serial
from conf import Conf
args = Conf("setting\config.json")

# add data to response
def resdata(dec)->bytearray:
    buf = bytearray()
    buf += dec.to_bytes(1,byteorder='big') # add lead byte
    if dec == 208:
        buf += str(random.randrange(1,4)).encode()
    elif dec == 216 or dec == 217:
        buf += str(0).encode()
        buf += str(random.randrange(0,4)).encode()
    else:
        for i in range(2):
            buf += str(0).encode()
        buf += str(random.randrange(0,9)).encode()
        buf += str(random.randrange(0,9)).encode()
    return buf

# Add data to dictionary
command = {}
def newdata():
    for i in range(160,173):
        command[i] = (i+16).to_bytes(1,byteorder='big')
    for i in range(192, 206):
        command[i] = resdata(i+16)
newdata()
print (command)

ser = serial.Serial(
    port = args["readPort"], 
    baudrate=args["rate"],
    parity=args["Parity"],
    stopbits=args["stopbits"],
    bytesize=args["bytes"], 
     timeout=args["timeout"], 
    )


# parse incoming string


print (ser.name)
while True:        
    if(ser.in_waiting > 0):
        mes = ser.readline()
        print(mes)
        # parse hex
        req = (int(mes[0])) #key
        reqd = ((mes[1:].decode())) #value
        print (req, ':', reqd, " : ", command[req])
        # use key to get response
        if req in command:
            ser.write (command[req])
        else:
            ser.write (   (191).to_bytes(1,byteorder='big') )
        
        newdata()


