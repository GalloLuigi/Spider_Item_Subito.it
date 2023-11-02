# from tutorial : https://www.youtube.com/watch?v=2vWCzB9HBgk   time:21.12

import tkinter as tk
import tkinter.ttk as TTK
from PIL import ImageTk, Image


from data.brands import brands
from data.regions import regions


def find_cars():
    """
    define find cars
    text = "try try"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, padx=100, pady=20)
    """


window = tk.Tk()
window.geometry("500x300")
window.title("Subito.it Spider")
#window.resizable(False, False)
#window.grid_columnconfigure(0, weight=1)







#window.configure(background="blue")


title_label = tk.Label(window, text="Subito.it Web Spider", font=("System", 20))
title_label.grid(row=0, column=1, sticky="N", padx=30, pady=10)

title_label = tk.Label(window, text="Car name:", font=("System", 15))
title_label.grid(row=1, column=0, padx=5, pady=10)

text_input = tk.Entry(width=30)
text_input.grid(row=1, column=1, padx=5, pady=10)
# text_input.get() ottine quello scritto nel item


title_label = tk.Label(window, text="Brand name:", font=("System", 15))
title_label.grid(row=3, column=0, padx=5, pady=10)

combo = TTK.Combobox(window, value=brands)
combo.grid(row=3, column=1, padx=100, pady=20)
""""
frame = tk.Frame(window, width=1, height=1)
frame.grid(row=3, column=2)

img = ImageTk.PhotoImage(Image.open("./utility/images/car-icon.jpg"))
label = tk.Label(frame, image=img)
label.grid(row=3, column=2)
"""""

title_label = tk.Label(window, text="Region name:", font=("System", 15))
title_label.grid(row=4, column=0, padx=5, pady=10)

combo = TTK.Combobox(window, value=regions)
combo.grid(row=4, column=1, padx=100, pady=20)

find_button = tk.Button(text="Find", command=find_cars)
find_button.grid(row=5, column=1, padx=100, pady=20,sticky="WE")


if __name__ == "__main__":
    window.mainloop()
