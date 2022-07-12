import shutil
import string

import PyInstaller

import subprocess
import winapps
import PySimpleGUI as sg
import os.path
import ctypes

file_list_column = [
    [
        sg.Text("File Path"),
        sg.In(size=(25, 1), enable_events=True, key="-File Path-"),
        sg.Button(size=(10, 1), enable_events=True, key="-AddButton-", button_text="Add"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-File List-"
        )
    ],
    [
        sg.Button(size=(15, 1), enable_events=True, key="-create-", button_text="Create")
    ],
]

layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("Startup Script", layout)
subInput = ""
subnum = 0
file_list = []

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "-AddButton-":
        new_filename = values["-File Path-"].strip()
        if new_filename not in file_list:
            file_list = sorted(file_list + [new_filename])
            print(file_list)
            values = file_list
            window["-File List-"].update(values)
        for inputs in file_list:
            subInput = "subprocess.Popen(r'" + inputs + "')\n"
            print("added to file")
        filename = "subprocess" + str(subnum) + ".py"
        if not os.path.exists(filename):
            f = open(filename, "x")
            f.write("import subprocess\n")
            f.write(new_filename)
            f.close()
    elif event == "-create-":
        print("create")
        installPath = os.path.abspath(filename)
        os.system('cmd /k"PyInstaller" ' + installPath)
        subnum = subnum + 1

window.close()
# subprocess.Popen(r"C:\Users\templ\AppData\Local\Discord\app-1.0.9004\Discord.exe")
# subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe")
