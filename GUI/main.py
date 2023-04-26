import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wetterbox | GUI")
        self.geometry("1080x720")
        self.resizable(False, False)
        self.create_frames()
        self.create_menu()
        self.create_dashboard_widgets()

    def create_frames(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, anchor="nw")


    def create_menu(self):

        self.menu = ttk.Notebook(self.main_frame)
        self.menu.pack(expand=True, fill="both", anchor="nw")

        self.dashboard_frame = ttk.Frame(self.menu)
        self.dashboard_frame.pack()
        self.menu.add(self.dashboard_frame, text="Dashboard")

    def create_dashboard_widgets(self):
        self.dashboard_infotext_temp_boden = ttk.Label(self.dashboard_frame, text="Temperatur Boden: ")
        self.dashboard_infotext_temp_boden.grid(row=0, column=0, sticky="w")

        self.dashboard_infotext_temp_luft = ttk.Label(self.dashboard_frame, text="Temperatur Luft: ")
        self.dashboard_infotext_temp_luft.grid(row=1, column=0, sticky="w")

        self.dashboard_infotext_luftfeuchte = ttk.Label(self.dashboard_frame, text="Luftfeuchte: ")
        self.dashboard_infotext_luftfeuchte.grid(row=2, column=0, sticky="w")

        self.dashboard_infotext_bodenfeuchte = ttk.Label(self.dashboard_frame, text="Bodenfeuchte: ")
        self.dashboard_infotext_bodenfeuchte.grid(row=3, column=0, sticky="w")

        self.dashboard_infotext_temp_erde = ttk.Label(self.dashboard_frame, text="Temperatur Erde: ")
        self.dashboard_infotext_temp_erde.grid(row=4, column=0, sticky="w")

        self.dashboard_infotext_sonnenlicht = ttk.Label(self.dashboard_frame, text="Sonnenintensität: ")
        self.dashboard_infotext_sonnenlicht.grid(row=5, column=0, sticky="w")

        self.dashboard_infotext_regen = ttk.Label(self.dashboard_frame, text="Regenintensität: ")
        self.dashboard_infotext_regen.grid(row=6, column=0, sticky="w")

        self.dashboard_infotext_windspeed = ttk.Label(self.dashboard_frame, text="Windgeschwindigkeit: ")
        self.dashboard_infotext_windspeed.grid(row=7, column=0, sticky="w")

        self.dashboard_infotext_windrichtung = ttk.Label(self.dashboard_frame, text="Windrichtung: ")
        self.dashboard_infotext_windrichtung.grid(row=8, column=0, sticky="w")

        self.dashboard_infotext_luftdruck = ttk.Label(self.dashboard_frame, text="Luftdruck: ")
        self.dashboard_infotext_luftdruck.grid(row=9, column=0, sticky="w")

        self.dashboard_infotext_temp_system = ttk.Label(self.dashboard_frame, text="Systemtemperatur: ")
        self.dashboard_infotext_temp_system.grid(row=10, column=0, sticky="w")

        self.dashboard_infotext_temp_cpu = ttk.Label(self.dashboard_frame, text="CPU-Temperatur: ")
        self.dashboard_infotext_temp_cpu.grid(row=11, column=0, sticky="w")

        self.dashboard_infotext_lüfterstatus_außen = ttk.Label(self.dashboard_frame, text="Lüfterstatus außen: ")
        self.dashboard_infotext_lüfterstatus_außen.grid(row=12, column=0, sticky="w")

        # Belüftung für Temperatursensor im wettergeschützten Bereich
        self.dashboard_infotext_lüfterstatus_innen = ttk.Label(self.dashboard_frame, text="Lüfterstatus innen: ")
        self.dashboard_infotext_lüfterstatus_innen.grid(row=13, column=0, sticky="w")

        # Belüftung für Raspberry und Temperatursensor "System"
        self.dashboard_infotext_lüfterstatus_system = ttk.Label(self.dashboard_frame, text="Lüfterstatus System: ")
        self.dashboard_infotext_lüfterstatus_system.grid(row=14, column=0, sticky="w")






if __name__ == "__main__":
    window = Window()
    window.mainloop()