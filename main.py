import pickle
import tkinter

from gui import Button, Entry
from investment_objects import Portfolio
from investment_objects import Investor
from system import System

def create_investor():
    first_name = inv_first_name.get()
    last_name = inv_last_name.get()

    if first_name == "" or last_name == "":
        msg = "No investor was created."
    else:
        inv = Investor(first_name=inv_first_name.get(), last_name=inv_last_name.get())
        system.save_investor(inv)

        msg = "Investor '" + inv.name + "' was created."

        inv_first_name.delete(0, tkinter.END)
        inv_last_name.delete(0, tkinter.END)

    label_status["text"] = msg


root = tkinter.Tk()
root.title("Portfolio Analyzer 1.0")

# set up the system
system = System()

# Investor entry fields
inv_first_name = Entry(master=root)
inv_first_name.pack()
inv_last_name = Entry(master=root)
inv_last_name.pack()

# Button to create investor
btn_inv = Button(master=root, text="Create investor",
                 command=lambda: create_investor())
btn_inv.pack()


# Status message fields
label_status = tkinter.Label(root, text="")
label_status.pack()
#
# # create portfolios and assign to investor
# pf01 = Portfolio(name="my first portfolio", id="xyz123", owner=inv)
# pf02 = Portfolio(name="my second portfolio", id="abc123", owner=inv)
#
# # load test data into pf
# pf01.load()

# # print pf holdings
# print(pf01.holdings)
#
# # print all portfolios of investor
# for key, value in inv.portfolios.items():
#     print("Portfolio ID: " + key)
#     print("Portfolio name: " + value.name)
#     print("Portfolio owner: " + value.owner.name)
#     print("-" * 30)

root.mainloop()