from pynput.keyboard import Key, Controller
import time
import tkinter as tk


hidden = True
keyboard = Controller()
shift = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"]
originals = {"~" : "`",
             "!" : "1",
             "@" : "2",
             "#" : "3",
             "$" : "4",
             "%" : "5",
             "^" : "6",
             "&" : "7",
             "*" : "8",
             "(" : "9",
             ")" : "0",
             "_" : "-",
             "+" : "=",
             "{" : "[",
             "}" : "]",
             "|" : "\\",
             ":" : ";",
             '"' : "'",
             "<" : ",",
             ">" : ".",
             "?" : "/"
             }


def type_phrase():
    time.sleep(float(delayentry.get()))
    input = textentry.get()
    for each in str(input):
        time.sleep(float(chardelay.get()))
        if each != " ":
            if each not in shift:
                keyboard.press(f'{each}')
                keyboard.release(f'{each}')
            else:
                with keyboard.pressed(Key.shift):
                    keyboard.press(f"{originals[each]}")
                    keyboard.release(f"{originals[each]}")
        else:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
    textentry.select_to(index=len(input))
    textentry.selection_clear()
    window.update()


def toggle_visible():
    global hidden
    global textentry
    if hidden:
        hidden = False
        textentry.configure(show="")
    else:
        hidden = True
        textentry.configure(show="*")


window = tk.Tk()
window.title("Copy/paste macro")
window.configure(background="gray")

tk.Label(window, text="Delay in Seconds: ", bg='grey', fg='black', font='none 12 bold').grid(row=0, column=0, sticky='W')
delayentry = tk.Entry(window, width=5, bg="white", fg='black', font='none 12')
delayentry.grid(row=0, column=1, sticky="W")
delayentry.insert(string='3', index=1)

tk.Label(window, text="Delay between letters: ", bg='grey', fg='black', font='none 12 bold').grid(row=1, column=0, sticky='W')
chardelay = tk.Entry(window, width=5, bg="white", fg='black', font='none 12')
chardelay.grid(row=1, column=1, sticky="W",)
chardelay.insert(string='0.05', index=1)

tk.Label(window, text="Text to copy: ", bg='grey', fg='black', font='none 12 bold').grid(row=2, column=0, sticky='W')
textentry = tk.Entry(window, width=30, bg="white", fg='black', font='none 12', show="*")
textentry.grid(row=2, column=1, sticky="W")

tk.Button(window, text="∅", width=1, command=toggle_visible, bg='white', fg='black', font="none 12 bold").grid(row=2,
            column=3)

tk.Button(window, text="submit", width=6, command=type_phrase, bg='white', fg='black', font="none 12 bold").grid(row=2,
            column=4)

window.mainloop()