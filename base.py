import tkinter as tk
import pyautogui as pg
import login as lg

root = tk.Tk()
root.attributes('-fullscreen', True)

generator = lg.login(root)
generator.scene1()






















root.mainloop()
