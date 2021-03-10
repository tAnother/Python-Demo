import tkinter as tk

class ktour:
    def __init__(self, master, n):
        ''' position info - variable '''
        self.cur_x = 0
        self.cur_y = 0

        ''' canvas info - constant '''
        self.master = master
        self.n = n
        self.grid_height = 50
        self.bound = n * self.grid_height

        self.canvas = tk.Canvas(master, width=self.bound, height=self.bound)      # create canvas
        self.init_canvas(n)         # fill the canvas
        self.canvas.pack()          # show in the window
        self.canvas.bind("<Button-1>", self.click_callback)

    def init_canvas(self, n):
        for i in range(n):
            for j in range(n): 
                self.draw_cell(i, j, "white")
        self.draw_cell(0, 0, "orange")


    def draw_cell(self, x, y, color):           
        ''' paint a cell '''
        self.canvas.create_rectangle(x*self.grid_height, y*self.grid_height, (x+1)*self.grid_height, (y+1)*self.grid_height, fill=color)

    def valid_move(self, new_x, new_y):
        ''' see if the knight can reach where we clicked '''
        if new_x >= self.n or new_x < 0 or new_y >= self.n or new_y < 0:        # not a grid
            return False

        if self.cur_x + 2 == new_x and self.cur_y + 1 == new_y:
            return True
        elif self.cur_x + 1 == new_x and self.cur_y + 2 == new_y:
            return True
        elif self.cur_x - 2 == new_x and self.cur_y - 1 == new_y:
            return True
        elif self.cur_x - 1 == new_x and self.cur_y - 2 == new_y:
            return True
        elif self.cur_x + 2 == new_x and self.cur_y - 1 == new_y:
            return True
        elif self.cur_x + 1 == new_x and self.cur_y - 2 == new_y:
            return True
        elif self.cur_x - 2 == new_x and self.cur_y + 1 == new_y:
            return True
        elif self.cur_x - 1 == new_x and self.cur_y + 2 == new_y:
            return True
        else:
            return False

    def click_callback(self, event):
        ''' called when click on the canvas '''
        new_x = event.x // self.grid_height     # clicked position
        new_y = event.y // self.grid_height

        if self.valid_move(new_x, new_y):
            self.draw_cell(self.cur_x, self.cur_y, 'blue')      # mark as visited
            self.draw_cell(new_x, new_y, 'orange')      # mark current position
            self.cur_x = new_x
            self.cur_y = new_y
        

def knights_tour(n):          
    ''' start the game '''
    root = tk.Tk()
    game = ktour(root, n)
    root.mainloop()

if __name__ == "__main__":
    knights_tour(5)