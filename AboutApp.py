# AboutApp.py
#Guled Abdi
#27/5/2025
#202502 spring
#Lab 8
#CIS 133 Y
# Description: This file implements the About tab, describing the app and the developers.

import os
import pygubu
import tkinter as tk

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "about.ui")


class AboutApp:
    def __init__(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        self.mainwindow = builder.get_object('about_top_frame', parent)

    def get_top_frame(self):
        return self.mainwindow


if __name__ == '__main__':
    root = tk.Tk()
    app = AboutApp(root)
    app.get_top_frame().pack(fill='both', expand=True)
    root.mainloop()
