import tkinter as tk
import tkinter.ttk as TTK


from data.brands import brands
from data.regions import regions
from core.basic_core import find_cars


def int_find_cars():
    return find_cars(combo_region.get(), combo_brand.get(), text_input.get(), find_button)


window = tk.Tk()
window.geometry("500x300")
window.title("Subito.it Spider")
window.resizable(False, False)

title_label = tk.Label(window, text="Subito.it Web Spider", font=("System", 20))
title_label.grid(row=0, column=1, sticky="N", padx=30, pady=10)

title_label = tk.Label(window, text="Car name:", font=("System", 15))
title_label.grid(row=1, column=0, padx=5, pady=10)

text_input = tk.Entry(width=30)
text_input.grid(row=1, column=1, padx=5, pady=10)


title_label = tk.Label(window, text="Brand name:", font=("System", 15))
title_label.grid(row=3, column=0, padx=5, pady=10)

combo_brand = TTK.Combobox(window, value=brands)
combo_brand.grid(row=3, column=1, padx=100, pady=20)

title_label = tk.Label(window, text="Region name:", font=("System", 15))
title_label.grid(row=4, column=0, padx=5, pady=10)

combo_region = TTK.Combobox(window, value=regions)
combo_region.grid(row=4, column=1, padx=100, pady=20)

find_button = tk.Button(text="Find", command=int_find_cars)
find_button.grid(row=5, column=1, padx=100, pady=20, sticky="WE")


if __name__ == "__main__":
    window.mainloop()
