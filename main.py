# MilesToKilometersApp.py
#Guled Abdi
#27/5/2025
#202502 spring
#Lab 8
#CIS 133 Y
# Description: This is the main entry point for Lab 8. It sets up a GUI with tabs for:
# About, Grams to Ounces, and Miles to Kilometers converters.

import tkinter as tk
from tkinter import ttk
import pygubu
from GramsToOuncesApp import GramsToOuncesApp
from AboutApp import AboutApp  # ✅ AboutApp imported

class MilesToKilometersApp:
    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('MilesToKilometersApp.ui')

        # Get the top frame from the UI
        self.mainwindow = builder.get_object('miles_to_km_top_frame', parent)

        # Connect button click event
        builder.connect_callbacks(self)

        # Access widgets
        self.miles_entry = builder.get_object('miles_entry')
        self.km_result_label = builder.get_object('km_result_label')

    def convert(self):
        try:
            miles = float(self.miles_entry.get())
            km = miles * 1.60934
            self.km_result_label.config(text=f'{km:.2f} kilometers')
        except ValueError:
            self.km_result_label.config(text='Invalid input')

    def get_top_frame(self):
        return self.mainwindow


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Unit Converter Lab 8")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=1, fill='both')

    # ✅ Tab 1 - About
    about_app = AboutApp(notebook)
    notebook.add(about_app.get_top_frame(), text="About")

    # ✅ Tab 2 - Grams to Ounces
    grams_app = GramsToOuncesApp(notebook)
    notebook.add(grams_app.get_top_frame(), text='Grams to Ounces')

    # ✅ Tab 3 - Miles to Kilometers
    miles_app = MilesToKilometersApp(notebook)
    notebook.add(miles_app.get_top_frame(), text='Miles to Kilometers')

    root.mainloop()