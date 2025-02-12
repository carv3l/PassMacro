from pynput.keyboard import Key, Listener
from pynput import keyboard


def on_press(key):

    if key == Key.ctrl_l:
        if key == Key.shift:
            print("{0} pressed".format(key))
        # if key == 190:


def on_activate():
    print("Global hotkey activated!")
    import passmacro


def for_canonical(f):
    return lambda k: f(l.canonical(k))


def on_release(key):

    # print("{0} release".format(key))
    if key == Key.esc:
        # Stop listener
        return False


hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<shift>+."), on_activate)

# # Collect events until released
# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


with keyboard.Listener(
    on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)
) as l:
    l.join()
