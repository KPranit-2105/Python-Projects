import random
import string
import PySimpleGUI as sg

sg.theme('Dark Amber 5')
sg.set_options(font='verdana 15')

layout = [
    [sg.Text('Uppercase: '), sg.Input(size=(15, 1), key='-UP-')],
    [sg.Text('Lowercase: '), sg.Input(size=(15, 1), key='-LOW-')],
    [sg.Text('Digits: '), sg.Input(size=(15, 1), key='-DIG-')],
    [sg.Text('Symbols: '), sg.Input(size=(15, 1), key='-SYM-')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Text('Password'), sg.Multiline(size=(15, 3), no_scrollbar=True, disabled=True, key='-PASS-')],
]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        try:
            u_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(values['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbols)

            total = upper + lower + digits + symbols
            total = random.sample(total, len(total))
            total = ''.join(total)
            window['-PASS-'].update(total)
        except ValueError:
            window['-PASS-'].update("No valid number")

window.close()
