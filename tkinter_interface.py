# from tutorial : https://www.youtube.com/watch?v=2vWCzB9HBgk   time:10.50

import tkinter as tk


def find_cars():
    text = "try try"
    text_output = tk.Label(window, text=text)
    text_output.grid(row=0,column=1)


window = tk.Tk()
window.geometry("800x600")
window.title("Subito.it Spider")
window.resizable(False, False)
# window.configure(background="white")


find_button = tk.Button(text="Find", command=find_cars)
find_button.grid(row=0, column=0)


if __name__ == "__main__":
    window.mainloop()
