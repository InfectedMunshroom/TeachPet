import tkinter as tk
import SnakeGame
root = tk.Tk()

root.attributes('-fullscreen',True)

def game():
    frame.destroy()
    SnakeGame.run()

frame = tk.Frame(root,bg='red',width='900',height='1440')
button = tk.Button(frame,text='Launch',command=SnakeGame.run)

frame.place(x=0,y=0)
button.place(x=25,y=25)




root.mainloop()
