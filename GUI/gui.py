import FreeSimpleGUI as sg
import runpy

sg.theme("DarkPurple")

list = open('GUI/labs.txt', 'r', encoding='utf-8').readlines()
label = sg.Text("Лабораторні роботи:")
list_box = sg.Listbox(values=list, key = "labs", enable_events = True, size=[45, 10])
field_box = sg.Listbox(values=[], key="field", enable_events=True, size=[44, 8])
                      
start_button = sg.Button("Запустити", key="Open")
exit_button = sg.Button("Вихід", key="Exit")
window = sg.Window("My GUI Program", 
                   layout=[
                       [label], 
                       [list_box, start_button],
                       [field_box],
                       [exit_button]
                       ], 
                   font=("Times New Roman", 20), 
                   size=(900, 700))
while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "Open":
        file_name = values["labs"][0].strip("\n")
        for el in file_name:
            num = el
        file = runpy.run_path(path_name=f'GUI/labs/lab{num}/lab{num}.py')
        window['field'].update(values=file)
    elif event == 'labs':
        file_name = values["labs"][0].strip("\n")
        for el in file_name:
            num = el
        file = open(f'GUI/labs/lab{num}/README.md', 'r', encoding='utf-8').readlines()
        window['field'].update(values=file)
#'GUI\\'+file_name+'.py'
print('Completed')
window.close()