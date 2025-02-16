from pynput.keyboard import Key, Listener
from pynput import keyboard
from passmacro import App
import tkinter as tk
import threading

def on_press(key):

    if key == Key.ctrl_l:
        if key == Key.shift:
            print("{0} pressed".format(key))
        # if key == 190:


def run_gui():
    root = tk.Tk()
    app = App(root)


    root.lift()  # Raise window above all others
    root.attributes('-topmost', 1)  # Keep it on top
    root.after(500, lambda: root.attributes('-topmost', 0))

    root.bind("<FocusOut>", lambda event: root.destroy())



    root.mainloop()


def on_activate():
    print("Global hotkey activated!")

    gui_thread = threading.Thread(target=run_gui, daemon=True)
    gui_thread.start()


def for_canonical(f):
    return lambda k: f(l.canonical(k))  


def on_release(key):

    print("{0} release".format(key))
    if key == Key.esc:
        # Stop listener
        return False


hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<shift>+."), on_activate)

# # Collect events until released
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


with keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)) as l:
    l.join()


#cd .\PassMacro\ ; .\venv\Scripts\activate ; py shortcut_list.py
