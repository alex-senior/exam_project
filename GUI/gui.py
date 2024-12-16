import FreeSimpleGUI as sg
import os

sg.theme("DarkPurple")

list = open('GUI/labs.txt', 'r', encoding='utf-8').readlines()
label = sg.Text("Labs")
list_box = sg.Listbox(values=list, key = "labs", enable_events = True, size=[45, 10])
                      
start_button = sg.Button("Open")
exit_button = sg.Button("Exit")
window = sg.Window("My GUI Program", 
                   layout=[
                       [label], 
                       [list_box, start_button],
                       [exit_button]
                       ], 
                   font=("Times New Roman", 20), 
                   size=(900, 700))
while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "Open":
        file_name = list(values["labs"][0].strip("\n"), reverse=True)
        print (file_name)
#'GUI\\'+file_name+'.py'
print('Completed')
window.close()