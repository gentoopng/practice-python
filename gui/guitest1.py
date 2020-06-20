import tkinter

root = tkinter.Tk()
root.title("GUI test")
root.geometry("600x400")

label = tkinter.Label(root, text="This is the label.")
label.grid()

root.mainloop()