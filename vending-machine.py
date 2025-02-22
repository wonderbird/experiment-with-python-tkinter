# This file shows the UI of the vending machine described in
# Guy Royse: Vending Machine Kata
# https://github.com/guyroyse/vending-machine-kata

from tkinter import *
from tkinter import ttk

class UserInterface:
    def __init__(self, root):
        root.title("Vending Machine")
        frame = ttk.Frame(root)
        frame.grid(column=0, row=0, sticky=(N, W, E, S))

        balanceLabel = ttk.Label(frame, text="Your balance:")
        balanceLabel.grid(column=1, row=1, sticky=E)
        balance = ttk.Label(frame, text="0.00")
        balance.grid(column=2, row=1, sticky=(W, E))

        messageLabel = ttk.Label(frame, text="Message:")
        messageLabel.grid(column=1, row=2, sticky=E)
        message = ttk.Label(frame, text="INSERT COIN")
        message.grid(column=2, row=2, sticky=(W, E))

        penny = ttk.Label(frame, text="Penny")
        penny.grid(column=1, row=3, sticky=(W, E))
        nickel = ttk.Label(frame, text="Nickel")
        nickel.grid(column=2, row=3, sticky=(W, E))
        dime = ttk.Label(frame, text="Dime")
        dime.grid(column=3, row=3, sticky=(W, E))
        quarter = ttk.Label(frame, text="Quarter")
        quarter.grid(column=4, row=3, sticky=(W, E))

        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)


def main():
    root = Tk()
    UserInterface(root)
    root.mainloop()


if __name__ == '__main__':
    main()
