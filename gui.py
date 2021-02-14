import tkinter

if __name__ == '__main__':


    root = tkinter.Tk()
    root.title("Neptunhiker's portfolio analysis")

    # LABELS
    # my_label1 = tkinter.Label(root, text="Hello world")
    # my_label2 = tkinter.Label(root, text="Hello again from me")
    #
    # my_label1.grid(row=0, column=0)
    # my_label2.grid(row=1,column=1)

    # INPUT
    entry = tkinter.Entry(root, width=70, bg="grey")
    entry.pack()
    entry.insert(0, "Enter your name")


    # BUTTONS
    def myClick():
        msg = "Hello " + entry.get()
        label = tkinter.Label(root, text=msg)
        label.pack()

    my_button = tkinter.Button(root, text="Click me", padx=30, pady=50,
                               command=myClick,
                               bg="black", fg="white")



    my_button.pack()




    root.mainloop()

else:

    class Gui:

        fg = "red"
        bg = "yellow"
        def __init__(self):
            self.fg = "white"
            self.bg = "black"


    class Entry(tkinter.Entry, Gui):

        def __init__(self, master, width=50):
            super().__init__(master=master, width=width, fg=super().fg, bg=super().bg)

    class Button(tkinter.Button, Gui):

        def __init__(self, master, text, command):
            super().__init__(master=master, text=text, command=command, fg=super().fg, bg=super().bg, padx=10, pady=10)





