import tkinter as tk
import tkinter.font as tkfont
from tkinter import *


class App:

    def __init__(self, root):
        self.root = root

        self.root.title("Password Macro")
        heigth = 720
        width = 1280
        screenheight = root.winfo_screenheight()
        screenwidth = root.winfo_screenwidth()
        alignstr = "%dx%d+%d+%d" % (
            width,
            heigth,
            (screenwidth - width) / 2,
            (screenheight - heigth) / 2,
        )
        root.geometry(alignstr)
    # root.resizable(width=False, heigth=False)

        

        print( round((screenwidth - width)/ 4))
        print(round((screenwidth - heigth)/ 20))

        Searchbar = Entry(root,bd =0, text= "Search",font=('arial',40,'bold'),width = 25, bg='lightgrey')
      
        Searchbar.place(relx=.5, rely=.1, anchor='center')
        Searchbar.focus_set()

        self.SearchString = StringVar(Searchbar, "")
        Searchbar.config(textvariable = self.SearchString)

        SearchResultBar = Label(root)
        SearchResultBar.pack()


            
        Searchbar.bind('<Return>', self.DisplaySearchResult, add = '+')
        Searchbar.bind('<FocusOut>', self.DisplaySearchResult, add = '+')

        
    def DisplaySearchResult(self, *args):
        Keyword = self.SearchString.get()

        print(Keyword)
       # {write some code to search your csv data and get a string to describe the search result, which we'll call SearchResult}
       # SearchString.set(SearchResult)

if __name__ == "__main__":
       root = tk.Tk()
       app = App(root)
       root.mainloop()



#  cd .\bitbucket\ ; .\venv\Scripts\activate ; cd '.\Side Projects\' ; py .\passmacro.py



