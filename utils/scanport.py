# import sys
# import glob
# import serial

# def serial_ports():
#     """ Lists serial port names

#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/tty[A-Za-z]*')
#     elif sys.platform.startswith('darwin'):
#         ports = glob.glob('/dev/tty.*')
#     else:
#         raise EnvironmentError('Unsupported platform')

#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except (OSError, serial.SerialException):
#             pass
#     return result

# if __name__ == '__main__':
#     print(serial_ports())


# import win32com.client
# wmi = win32com.client.GetObject("winmgmts:")
# for serial in wmi.InstancesOf("Win32_SerialPort"):
#     a = serial.Name
#     b = a[a.index("(") + 1:a.rindex(")")]
#     print (b, " : ", serial.Name, serial.Description)

import serial.tools.list_ports

def scanner ()->object:
    ports = list(serial.tools.list_ports.comports())
    return ports

def pickPort()->None:
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB Serial Port' in p.description:
            if p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")] == "0403":
                print("found")
                # Connection to port

                a = p.hwid
                b = p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")]
                return p.device
                
        return None #args["writePort"]


if __name__ == "__main__":
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)
        if 'USB Serial Port' in p.description:
            if p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")] == "0403":
                print("found")
                # Connection to port

                a = p.hwid
                b = p.hwid[p.hwid.index("PID") + 4:p.hwid.rindex(":")]
                print (p.device)