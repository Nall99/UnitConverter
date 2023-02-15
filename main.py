import PySimpleGUI as sg
sg.theme('DarkAmber')
font = ('Calibri', 15)
layout = [
    [sg.Input(key='input',enable_events=True, font=font, justification='center',size=(20,1)),sg.Text('',key='output', font=font, justification='center',size=(20,1))],
    [sg.Combo(['Fahrenheit', 'Kelvin', 'Celsius'],size=(20,1),enable_events=True,font=font, default_value='Fahrenheit',key='current_unit',readonly=True),sg.Combo(['Fahrenheit', 'Kelvin', 'Celsius'],enable_events=True,size=(20,1),font=font, default_value='Fahrenheit',key='to_unit',readonly=True)]
]
window = sg.Window('Unit Converter', layout, size=(570,90))

result = 0

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    # if empty
    if value['input'] == '':
        value['input'] = '0'
    else:
        window['input'].update(value['input'])
    
    # if not a number
    if event == 'input' and value['input'][-1] not in ('1','2','3','4','5','6','7','8','9','0','.'):
        window['input'].update(value['input'][:-1])

    # Farenheit
    if value['current_unit'] == 'Fahrenheit':
        # to kelvin
        if value['to_unit'] == 'Kelvin':
            result = (int(value['input']) - 32) * 5/9 + 273.15
        # to celsius
        elif value['to_unit'] == 'Celsius':
            result = (int(value['input']) - 32) * 5/9
    # Celsius
    elif value['current_unit'] == 'Celsius':
        # to fahrenheit
        if value['to_unit'] == 'Fahrenheit':
            result = (int(value['input']) * 9/5) + 32
        # to kelvin
        elif value['to_unit'] == 'Kelvin':
            result = int(value['input']) + 273.15
    # Kelvin
    elif value['current_unit'] ==  'Kelvin':
        # to celsius
        if value['to_unit'] == 'Celsius':
            result = int(value['input']) - 273.15
        # to fahrenheit
        elif value['to_unit'] == 'Fahrenheit':
            result = (int(value['input']) - 273.15) * 9/5 + 32

    # update output display
    window['output'].update(f'{result:.3f}')

window.close()