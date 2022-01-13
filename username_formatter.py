import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Turning list of names into SQL list')],
          [sg.Text('Enter list of usernames from roster')],
          [sg.Multiline(size=(35, 35)),
          sg.Output(size=(35, 10), key='-OUTPUT-')],
          [sg.Button('Format'), sg.Button('Cancel')]]

window = sg.Window('SQL Roster Username Formatter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    users = values[0].lower().splitlines()
    new_users = []
    for user in users:
        new_user = "'" + user + "',"
        new_users.append(new_user)
    last_element = new_users[-1].replace(',', '')
    del new_users[-1]
    new_users.append(last_element)

    if event == 'Format':
        window['-OUTPUT-'].Update('')
        for user in new_users:
            print(user)

window.close()
