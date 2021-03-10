
import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent

        self.push_count = 0

        self.button = tk.Button(
            self, 
            text = 'Character Window', 
            command = self.new_window,
            height = 10,
            width = 50)
        self.button.pack()

        self.push_counter = tk.Button(
            self, 
            text = 'You need to click me', 
            command = self.push_me,
            height = 10,
            width = 50)
        self.push_counter.pack()

    def new_window(self):
        self.button['state'] = tk.DISABLED
        self.newWindow = tk.Toplevel(self)
        self.newWindow.geometry("500x500") #change the width and height provided to geometry() function
        self.newWindow.resizable(0,0) #Don't allow resizing in the x or y direction
        CharWindow(self) #pass the entire self class

    def push_me(self):
        self.push_count += 1
        self.push_counter['text'] = "you pushed me %d times"%self.push_count

class CharWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.newWindow) 
        self.pack()
        self.parent = parent

        self.push_count = 0

        self.quitButton = tk.Button(
            self, 
            text = 'Quit',
            command = self.close_windows,
            height = 10,
            width = 50)
        self.quitButton.pack()

        self.push_counter = tk.Button(
            self, 
            text = 'You need to click me', 
            command = self.push_me,
            height = 10,
            width = 50)
        self.push_counter.pack()
        
        # this is new
        self.button = tk.Button(self, text = 'New Window', 
                                command = self.new_window,
                                height = 10,
                                width = 50)
        self.button.pack()
        # this is new

    def close_windows(self):
        self.parent.button['state'] = tk.NORMAL #so now you have the MainScreen instance available as self.parent
        self.parent.newWindow.destroy()

    def push_me(self):
        self.push_count += 1
        self.push_counter['text'] = "you pushed me %d times"%self.push_count
    
    # this is new
    def new_window(self):
        self.button['state'] = tk.DISABLED
        self.newWindow = tk.Toplevel(self)
        CharWindow(self) #pass the entire self class
    # this is new


def main(): 
    root = tk.Tk()
    root.title('My Application')
    root.geometry("500x300") #change the width and height provided to geometry() function
    root.resizable(0,0) #Don't allow resizing in the x or y direction
#     root.minsize(400, 300) # or setting the minimun size of the root window 
    app = MainScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()