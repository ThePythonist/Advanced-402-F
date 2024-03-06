import tkinter

window = tkinter.Tk()
window.title("My Window")
window.geometry("500x300")
window.resizable(width=False, height=False)
window.configure(background="#c54619")


def report():
    print("clicked submit button")


# mylabel = tkinter.Label(window, text="Welcome").pack(anchor="s", side="right")
# mylabel = tkinter.Label(window, text="Welcome",bg="red").pack(fill="both", expand=True)
mybutton = tkinter.Button(window, text="Submit", command=report).pack()
window.mainloop()
