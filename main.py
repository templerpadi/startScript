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
    elif event == "-create-":
        print("create")
        for inputs in file_list:
            subInput = "subprocessFile.Popen(r" + inputs + ")\n"
            print("added to file")
            filename = "subprocessFile" + str(subnum) + ".py"
            if not os.path.exists(filename):
                f = open(filename, "x")
                f.write(subInput)
                f.close()
                subnum = subnum + 1
            else:
                subnum = subnum + 1
        installPath = os.path.abspath(filename)
        os.system("PyInstaller" + installPath)

window.close()
