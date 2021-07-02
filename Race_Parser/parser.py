from tkinter import *
from tkinter import ttk
from get_data import get_data
from treeview import to_view


if __name__ == "__main__":
    app = Tk()
    app.title("Parser")
    app.geometry('550x550')
    # app.resizable(width=1000, height=1000)
    ttk.Label(app, text="Treeview").pack()
    treeview = ttk.Treeview(app, selectmode='browse')
    treeview.column('#0', width=500, stretch='no')
    treeview.pack()
    verscrlbar = ttk.Scrollbar(app,
                               orient="vertical",
                               command=treeview.yview)
    verscrlbar.pack(side='right', fill='x')

    # Configuring treeview
    treeview.configure(xscrollcommand=verscrlbar.set)
    data = get_data('./testfiles/sweets.yaml', 'yaml')
    to_view(data, treeview, 'json', '')

    app.mainloop()