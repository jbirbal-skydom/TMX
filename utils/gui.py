import tkinter as tk
from tkinter import ttk
import awesometkinter as atk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.config(background=atk.DEFAULT_COLOR)

        # it is recommended to select tkinter theme required for things to be right on windows,
        # 'alt', 'default', or 'classic' work fine on windows
        s = ttk.Style()
        s.theme_use('default')

        showinfo("Welcome", "Any issues please contact Jason @ skydom@zoho.com")
        

        # 3d frame
        f1 = atk.Frame3d(self)
        f1.pack(side='left', expand=True, fill='both', padx=3, pady=3)

        self.elevinc = atk.Button3d(f1, text='+ Elev +')
        self.elevinc.pack(pady=10)

        # 3d progressbar Elev
        self.elevbar = atk.RadialProgressbar3d(f1, fg='cyan', size=120)
        self.elevbar.pack(padx=20, pady=20)
        self.elevbar.setval = 0
        self.elevbar.units = " %"
        self.elevbar.set(0)

        # 3d button
        self.elevdec = atk.Button3d(f1, text='- Elev -')
        self.elevdec.pack(pady=10)

        f2 = atk.Frame3d(self)
        f2.pack(side='left', expand=True, fill='both', padx=3, pady=3)

        self.spdinc = atk.Button3d(f2, text='+ Speed +' )
        self.spdinc.pack(pady=10)
        self.spdinc['command'] = lambda: self.button_clicked(self.spdinc.cget('text'))

        # flat radial progressbar for speed
        self.spdbar = atk.RadialProgressbar(f2, fg='green')
        self.spdbar.pack(padx=30, pady=30)
        self.spdbar.setval = 0
        self.spdbar.units = " MPH"
        self.spdbar.set (20)
    

        # 3d button
        self.spddec = atk.Button3d(f2, text='- Speed -', command = self.someAction )
        self.spddec.pack(pady=10)


    def button_clicked(self, name):
        showinfo(title='Information', message=name)
    def someAction(self):
        my_text = self.spddec.cget('text')
        print(my_text)


if __name__ == "__main__":
  app = App()
  app.mainloop()
