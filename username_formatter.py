import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Turning list of names into SQL list')],
          [sg.Text('Enter list of usernames from roster')],
          [sg.Multiline(default_text='bCalderon2', size=(35, 35)),
          sg.Output(size=(35, 10), key='-OUTPUT-')],
          [sg.Button('Format'), sg.Button('Cancel'), sg.Button('About')]]

window = sg.Window('SQL Roster Username Formatter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Format' and len(values[0]) > 0:

        try:
            users = values[0].lower().splitlines()
            new_users = []
            for user in users:
                new_user = "'" + user + "',"
                new_users.append(new_user)
            last_element = new_users[-1].replace(',', '')
            del new_users[-1]
            new_users.append(last_element)
            window['-OUTPUT-'].Update('')

            for user in new_users:
                print(user)

        except Exception as e:
            print(e)

    if event == 'About':
        sg.Popup('About', 'Created by Ballardo Calderon',
                 'https://github.com/BSCalderon/SQL-Formatter', 'Version: 1.02')

window.close()
