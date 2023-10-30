# from tutorial : https://www.youtube.com/watch?v=2vWCzB9HBgk   time:21.12

import tkinter as tk


def find_cars():
    text = "try try"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica",16))
    text_output.grid(row=1, column=1, padx=100, pady=20)


window = tk.Tk()
window.geometry("800x600")
window.title("Subito.it Spider")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
# window.grid_columnconfigure(1, weight=1)
# window.grid_rowconfigure(0, weight=1)
#window.grid_rowconfigure(1, weight=1)




# window.configure(background="white")


title_label = tk.Label(window, text="Subito.it Web Spider", font=("Helvetica", 15))
title_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

# find_button = tk.Button(text="Find", command=find_cars)
# find_button.grid(row=0, column=0, padx=100, pady=20)


if __name__ == "__main__":
    window.mainloop()
