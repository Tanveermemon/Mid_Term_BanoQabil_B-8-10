# @@ -1,5 +1,4 @@
# i want to import path string from path library of python
from pathlib import Path
# this will import the layout and theme.
import PySimpleGUI as sg
# to import pandas for coverting data into excel sheet or any third standalone software.
import pandas as pd

# Add some color to the windowPySimpleGUI is a Python package that provides a simple and lightweight interface for creating graphical user interfaces (GUIs). 
# 'DarkAmber'
# 'DarkBlue'
# 'DarkBrown1'
# 'DarkGreen1'
# 'DarkGrey1'
# 'DarkPurple'
# 'DarkRed'
# 'DarkTeal'
# 'LightBlue'
# 'LightGreen'
sg.theme('LightBlue')

current_dir = Path('D:\\Docs\\Python\\data_entry5.xlsx').parent if 'D:\\Docs\\Python\\data_entry5.xlsx' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'data_entry5.xlsx'
df = pd.read_excel(EXCEL_FILE)

# Load the data if the file exists, if not, create a new DataFrame
if EXCEL_FILE.exists():
    df = pd.read_excel(EXCEL_FILE)
else:
    df = pd.DataFrame()

layout = [
    [sg.Text('Please fill out your informations for Registration (Office wizard to Python course):', justification='center')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Father"s Name', size=(15,1)), sg.InputText(key='Father Name')],
    [sg.Text('Qualification', size=(15,1)), sg.Combo(['Matriculation', 'Intermediate', 'Bachelor', 'Master', 'Others'], key='Qualification')],
    [sg.Text('Age', size=(15,1)), sg.InputText(key='Age', text_color='yellow')],
    [sg.Text('Email', size=(15,1)), sg.InputText(key='Email')],
    [sg.Text('City', size=(15,1)), sg.InputText(key='City')],
    [sg.Text('Contact Number (Mobile)', size=(20,1)), sg.InputText(key='Contact Number (Mobile)')],
    [sg.Text('Days', size=(15,1)), sg.Combo(['Monday & Wednesday', 'Tuesday & Thursday'], key='Days')],
    [sg.Text('Time Slot', size=(15,1)),
                            sg.Checkbox('4:00 - 6:00 PM', key='First Shift'),
                            sg.Checkbox('6:00 - 8:00 PM', key='Second Shift'),
                            sg.Checkbox('8:00 - 10:00 PM', key='Third Shift')],
    [sg.Text('Your Roll Number is', size=(15,1)), sg.Spin([i for i in range(0,20)],
                                                       initial_value=0, key='Roll Number')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]
window = sg.Window('Bano Qabil 2.0 Registration Form', layout)
def clear_input():
    for key in values:
        window[key]('')
    return None
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        df.to_excel(EXCEL_FILE, index=False)  # This will create the file if it doesn't exist
        sg.popup('Once your data has been saved then no revert is possible!')
        clear_input()
window.close()