import tkinter as tk
import tkinter.font as tkfont
from pynput.keyboard import Key, Listener
from pynput import keyboard


root = tk.Tk()


class App:

    def __init__(self, root):
        root.title("Password Macro")
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

    # if __name__ == "__main__":
    #     root = tk.Tk()
    #     app = App(root)
    #     root.mainloop()

    def on_press(key):

        if key == Key.ctrl_l:
            if key == Key.shift:
                print("{0} pressed".format(key))
            # if key == 190:

    def on_activate():
        # print("Global hotkey activated!")
        app = App(root)
        root.mainloop()

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    def on_release(key):

        # print("{0} release".format(key))
        if key == Key.esc:
            # Stop listener
            return False


hotkey_en = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<shift>+."), App.on_activate)

with keyboard.Listener(
    on_press=App.for_canonical(hotkey_en.press),
    on_release=App.for_canonical(hotkey_en.press),
) as l:
    l.join()


#  cd .\bitbucket\ ; .\venv\Scripts\activate ; cd '.\Side Projects\' ; py .\passmacro.py



