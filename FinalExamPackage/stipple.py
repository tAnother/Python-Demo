# put your code here
import tkinter as Tk
import random as rd

class Stipple:
    def __init__(self, master):
        self.color = 'blue'
        self.shapes = []

        self.canvas = Tk.Canvas(master, width=500, height=500, bg='white')      # create canvas
        self.canvas.pack()          # show in the window
        self.canvas.bind("<Button-1>", self.click_callback)

        self.saveButton = Tk.Button(master, text="Save", command = self.save)
        self.saveButton.pack()
        self.loadButton = Tk.Button(master, text="Load", command = self.load)
        self.loadButton.pack()
        self.clearButton = Tk.Button(master, text="Clear", command = self.clear)
        self.clearButton.pack()
        self.changeButton = Tk.Button(master, text="Change Color", command = self.change)
        self.changeButton.pack()

    def click_callback(self, event):        
        x = event.x     # clicked position
        y = event.y 
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=self.color)
        self.shapes += [(x,y)]

    def save(self):
        with open ("./saved.txt", 'w') as savefile:
            savefile.write(self.color+"\n")
            for (x,y) in self.shapes:
                savefile.write(f"{x},{y}\n")

    def load(self):
        self.clear()
        with open ("./saved.txt", 'r') as readfile:
            data = readfile.read().rstrip("\n").split("\n")

        self.color = data[0]
        for xy in data[1:]:
            x = int(xy.split(",")[0])
            y = int(xy.split(",")[1])
            self.shapes += [(x,y)]

        for (x,y) in self.shapes:
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=self.color)

    def clear(self):
        self.canvas.delete('all')
        self.shapes = []

    def change(self):
        self.color = "#%06x" % rd.randint(0, 0xFFFFFF)
        for (x,y) in self.shapes:
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=self.color)


def main():
    root = Tk.Tk()
    root.title('Stipple Something')
    stipple = Stipple(root)
    root.mainloop()

if __name__ == '__main__':
    main()