# from tutorial : https://www.youtube.com/watch?v=2vWCzB9HBgk   time:21.12

import tkinter as tk
from data.brands import brands


def find_cars():
    """
    define find cars
    text = "try try"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, padx=100, pady=20)
    """

window = tk.Tk()
window.geometry("800x600")
window.title("Subito.it Spider")
window.resizable(False, False)
#window.grid_columnconfigure(0, weight=1)







#window.configure(background="blue")


title_label = tk.Label(window, text="Subito.it Web Spider", font=("System", 20))
title_label.grid(row=0, column=1, sticky="N", padx=30, pady=10)

title_label = tk.Label(window, text="Car name:", font=("System", 15))
title_label.grid(row=1, column=0, padx=5, pady=10)

text_input = tk.Entry(width=30)
text_input.grid(row=1, column=1, padx=5, pady=10)
# text_input.get() ottine quello scritto nel item

"""
Add a combobox

var = tk.StringVar()
cb_brands = tk.Combobox(window, textvariable=var)
cb_brands['values'] = brands
cb_brands['state'] = 'readonly'
cb_brands.pack(fill='x', padx=5, pady=5)
cb_brands.grid(row=2, column=1, padx=5, pady=10)
"""
find_button = tk.Button(text="Find", command=find_cars)
find_button.grid(row=3, column=0, padx=100, pady=20)


if __name__ == "__main__":
    window.mainloop()
