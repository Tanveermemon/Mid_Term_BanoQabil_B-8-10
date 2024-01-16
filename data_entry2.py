# this will import the layout and theme.
import PySimpleGUI as sg

# import pandas as pd
# Add a touch of color
sg.theme('DarkAmber')

# EXCEL_FILE = "D:\Docs\Python\data_entry.xlsx"

# df = pd.read_excel(EXCEL_FILE)

# All the stuff inside your window.
layout = [  
    [sg.Text('Registration Form for Bano Qabil Admission')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Batch#', size=(15,1)), sg.Combo(['3-6', '6-8', '8-10'], key='Batch Number')],
    [sg.Text('Course Name', size=(15,1)),
                        sg.Checkbox('Office Wizar to Python', key='Course # 01 (Office Wizar to Python)'),
                        sg.Checkbox('Web Development', key='Course # 02 (Websit Development'),
                        sg.Checkbox('Basic SQL', key='Course # 03 (Basic SQL Language')],
    [sg.Text('Roll Number', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                    initial_value=0, key='Roll Number')],
    [sg.Submit(), sg.Exit()]
]
window = sg.Window('Bano Qabil 2.0', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
        # df = df.append(values, ignore_index=True)
        # df.to_excel(EXCEL_FILE, index=False)
        # sg.popup('Data saved!')
        
window.close()

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
# # if user close the window or click the cancel then code will be break
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         break
# # if user type anything and click Ok then data will be saved.    
#     print('You entered ', values[0])

# window.close()