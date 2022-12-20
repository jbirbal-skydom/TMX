from utils.gui import App
from utils.decode import com


request = {}
data = {}
data2 = {}

name2dec = {

    "start": 160,
    "forcestart":161 ,
    "stop":162 ,
    "speed":163 ,
    "elevation":164, 
    "time":165,
    "protocol":166,
    "stage":167,
    "reset":168,
    "weight":169,
    "autostop":170,
    "cool":171,
    "toggle":172

}

for i in range(160,173):
    request[i] = None
for i in range(192, 197):
    data[i] = None
for i in range(197, 206):
    data2[i] = None



def pulse(tx):
    connection.request_data(tx)
    app.after(400, lambda: pulse(data)) # add recurrent event
    app.after(1000, lambda: update(app.spdbar, data[195]))
    app.after(1000, lambda: update(app.elevbar, data[196]))


def update(module, raw):
    key, val = connection.info(raw)
    req = ( int(raw[0]))
    if 208 < req < 213 :
        val = val/10
    module.setval = val
    if key > 0: # get current val in percent
        _ , curval = connection.info(data[key])
        if curval != 0:
            percent = (min( val*10/curval, 1))*100
        else: 
             percent = 0
        module.set(percent)
        
def change(req ,_raw, increm = None, end_ = None):
    req = name2dec[req] # dec of req
    if end_ is not None:
        end_  = name2dec[end_]

    res = connection.send(command=req, raw=_raw, increment=increm, end = end_ )  # write to com
    request[req] = res # update dict





if __name__ == "__main__":

    connection = com()
    app = App()

    

    
    app.title('TMX') # Set title


    # app.after(100, newdata) #check or new data
    app.after(100, lambda: pulse(data)) #request new data

    
    app.elevinc['command'] = lambda: pulse(data)
    app.spddec['command'] = lambda: change("speed", data[195], increm=-5, end_="start" )
    app.spdinc['command'] = lambda: change("speed", data[195], increm=5, end_="start" )
    app.elevinc['command'] = lambda: change("elevation", data[196], increm=10, end_=None )
    app.elevdec['command'] = lambda: change("elevation", data[196], increm=-10, end_=None )
    
    app.mainloop()
    
    
    # while True:
    #     if (connection.ser.in_waiting > 0):
    #         print (connection.ser.readline())



