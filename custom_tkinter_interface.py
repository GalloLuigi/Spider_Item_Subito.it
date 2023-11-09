import tkinter
import tkinter.messagebox
import customtkinter

from core.basic_core import find_cars
from data.brands import brands
from data.regions import regions

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Subito.it Cars Spider")
        self.geometry(f"{600}x{350}")
        self.resizable(False, False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Cars Spider", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Support me")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Insert the name of the car...")
        self.entry.grid(row=2, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Find", command=self.int_find_cars())
        self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Main Info")
        self.tabview.tab("Main Info").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.combobox_0 = customtkinter.CTkComboBox(self.tabview.tab("Main Info"),
                                                    values=brands)
        self.combobox_0.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Main Info"),
                                                    values=regions)
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))




        # create tabview 2
        self.e_tabview = customtkinter.CTkTabview(self, width=250)
        self.e_tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.e_tabview.add("Extra Info")
        self.e_tabview.tab("Extra Info").grid_columnconfigure(1, weight=1)  # configure grid of individual tabs


        self.string_input_button = customtkinter.CTkButton(self.e_tabview.tab("Extra Info"), text="Enter displacement",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self.e_tabview.tab("Extra Info"), width=250)
        self.radiobutton_frame.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="n")

        self.radio_var = tkinter.IntVar(value=0)
        #self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="")
        #self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")



        # set default values

        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.combobox_0.set("Brand name")
        self.combobox_1.set("Region name")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Enter displacement:", title="Enter displacement")
        print("Enter displacement:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def int_find_cars(self):
        return find_cars(self.combobox_0.get(), self.combobox_1.get(), self.entry.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()