import tkinter
import asyncio
import threading
import websockets
from websockets import exceptions
import json
from datetime import datetime


event = 2

# Starthilfe für asynkrone Funktion connect
def _asyncio_thread():
    async_loop.create_task(connect())
    async_loop.run_forever()


async def connect():
    try:
        async with websockets.connect("wss://socketsbay.com/wss/v2/1/demo/") as websocket:
            while event > 1:
                message = await websocket.recv()
                print(message)
            print("stopping")
    except:
        print('connection')


async def send(websocket, name):
    while event > 1:
        msg = await queue.get()
        await websocket.send(msg)

def buttonexecutor(e=None):
    msg = entry.get()
    asyncio.run_coroutine_threadsafe(messagesender(msg), async_loop)
    entry.delete(0, "end")


async def messagesender(message):
    await queue.put(message)


def logger(reason, message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text.configure(state="normal")
    text.insert("end", f"({current_time}) [ {reason} ] {message}\n")
    text.configure(state="disabled")

def on_closing():
    event = 0
    async_loop.call_soon_threadsafe(async_loop.stop)
    thread.join()

    


if __name__ == '__main__':
    # Asyncio
    async_loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    # Erstelle tkinter
    root = tkinter.Tk()
    root.title("Messanger")

    text = tkinter.Text(root, width=150, state="disabled")
    text.pack()

    entry = tkinter.Entry(root, width=100)
    entry.insert("end", 'You email here')
    entry.pack()

    tkinter.Button(master=root, text="Senden", command=buttonexecutor).pack()

    # Starte Websocket Verbindung
    thread = threading.Thread(target=_asyncio_thread)
    thread.start()

    # Starte tkinter
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()