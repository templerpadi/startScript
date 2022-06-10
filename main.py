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


def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
        else:
            ctypes.windll.user32.MessageBoxW(0, "program not found", 1)
            break


window = sg.Window("Startup Script", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-AddButton-":
        filename = values["-File Path-"]
        print(filename)
        if filename != "[]":
            filePath = findfile(filename, "/")
            window["-File List-"].update(filePath)
        else:
            print("failed")
        print("worked")

window.close()

# subprocess.Popen(r"C:\Users\templ\AppData\Local\Discord\app-1.0.9004\Discord.exe")
# subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe")
