import subprocess
import winapps
import PySimpleGUI as sg
import os.path

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

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # file path input
    if event == "-File Path-":
        folder = values["-File Path-"]
        file_list = []
    # add button
        if event == "-Add-":
            window["-File List-"].update("subprocess.Popen(r'" + folder + "')")
            print("worked")

    elif event == "-File List-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-File Path-"], values["-File List-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close()

# subprocess.Popen(r"C:\Users\templ\AppData\Local\Discord\app-1.0.9004\Discord.exe")
# subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe")
