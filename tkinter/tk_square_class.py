import tkinter as tk

class RectangleGUI:
   def __init__(self, master):
	   self.master = master
	   self.canvas = tk.Canvas(master, width=500, height=500)
	   self.canvas.pack()
	   self.canvas.bind("<Button-1>", self.rectangle)
   def rectangle(self,ev):
	   self.canvas.create_rectangle(ev.x, ev.y, ev.x+20, ev.y+20, fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    gui=RectangleGUI(root)
    root.mainloop()