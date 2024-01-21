import PySimpleGUI as sg
import configparser

# Read the configuration from the file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the input values from the configuration
twitch_access_token = config.get('Twitch', 'access_token')
twitch_channel_id = config.get('Twitch', 'channel_id')
twitch_client_id = config.get('Twitch', 'client_id')
discord_access_token = config.get('Discord', 'access_token')
discord_channel_id = config.get('Discord', 'channel_id')

# Define the layout of the UI
layout = [
    [sg.Column([
        [sg.Text('Enter your Twitch API access token:')],
        [sg.Text('Enter your Twitch channel ID:')],
        [sg.Text('Enter your Twitch client ID:')],
        [sg.Text('Enter your Discord API access token:')],
        [sg.Text('Enter your Discord channel ID:')]
    ]),
    sg.Column([
        [sg.InputText(key='twitch_access_token', default_text=twitch_access_token)],
        [sg.InputText(key='twitch_channel_id', default_text=twitch_channel_id)],
        [sg.InputText(key='twitch_client_id', default_text=twitch_client_id)],
        [sg.InputText(key='discord_access_token', default_text=discord_access_token)],
        [sg.InputText(key='discord_channel_id', default_text=discord_channel_id)]
    ])
    ],
    [sg.Button('Save configuration')]
]

# Create the window
window = sg.Window('Twitch Clip Creator Configuration', layout)

# Event loop to process UI events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Save configuration':
        # Get the input values from the UI
        twitch_access_token = values['twitch_access_token']
        twitch_channel_id = values['twitch_channel_id']
        twitch_client_id = values['twitch_client_id']
        discord_access_token = values['discord_access_token']
        discord_channel_id = values['discord_channel_id']

        # Save the configuration to a file
        config = configparser.ConfigParser()
        config['Twitch'] = {
            'access_token': twitch_access_token,
            'channel_id': twitch_channel_id,
            'client_id': twitch_client_id
        }
        config['Discord'] = {
            'access_token': discord_access_token,
            'channel_id': discord_channel_id
        }
        with open('config.ini', 'w') as f:
            config.write(f)

        # Close the window
        window.close()
        break

# Close the window
window.close()
