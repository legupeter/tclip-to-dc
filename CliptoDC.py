import requests
import json
import configparser

# Read the configuration values from the INI file
config = configparser.ConfigParser()
config.read('config.ini')

twitch_access_token = config['Twitch']['access_token']
twitch_channel_id = config['Twitch']['channel_id']
twitch_client_id = config['Twitch']['client_id']
discord_access_token = config['Discord']['access_token']
discord_channel_id = config['Discord']['channel_id']

# Twitch API endpoint to create a clip
twitch_clip_endpoint = "https://api.twitch.tv/helix/clips"

# Discord API endpoint to post a message
discord_message_endpoint = f"https://discord.com/api/v9/channels/{discord_channel_id}/messages"

# Headers for Twitch API request
twitch_headers = {
    "Authorization": f"Bearer {twitch_access_token}",
    "Client-Id": twitch_client_id,
    "Content-Type": "application/json"
}

# Headers for Discord API request
discord_headers = {
    "Authorization": f"Bot {discord_access_token}",
    "Content-Type": "application/json"
}

# Parameters for Twitch API request
twitch_params = {
    "broadcaster_id": twitch_channel_id
}

# Create a clip on Twitch
response = requests.post(twitch_clip_endpoint, headers=twitch_headers, params=twitch_params)

# Get the clip ID from the response
clip_id = response.json()["data"][0]["id"]

# URL of the clip on Twitch
clip_url = f"https://clips.twitch.tv/{clip_id}"

# Message to post on Discord
message = {
    "content": f"New clip created on Twitch: {clip_url}"
}

# Post the message on Discord
requests.post(discord_message_endpoint, headers=discord_headers, data=json.dumps(message))

