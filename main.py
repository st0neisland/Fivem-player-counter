import requests
import json
import time

webhook_url = ""

players_url = "http://IP:30120/players.json"

def create_embed(player_count, player_names):
    embed = {
        "title": "Server Name",
        "description": f"Total players: {player_count}",
        "color": 16711680, 
        "fields": [
            {
                "name": "Players",
                "value": "\n".join(player_names)
            }
        ],
        "footer": {
            "text": "Update Time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
    }
    return embed

def send_discord_message(embed):
    payload = {
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 204:
        print("++")
    else:
        print("--", response.status_code)

def get_players_and_send_message():
    response = requests.get(players_url)
    players_data = response.json()

    player_count = len(players_data)
    player_names = [player['name'] for player in players_data]

    embed = create_embed(player_count, player_names)
    send_discord_message(embed)


def repeat(interval):
    while True:
        get_players_and_send_message()
        time.sleep(interval)

repeat(25)
Please note that the placeholder for "webhook_url" and "http://IP:30120/players.json" should be replaced with your actual webhook URL and the appropriate URL for your server's player data, respectively.





User
github için açıklama yani readme dosyası ve başlık oluştururmusun
ChatGPT
Certainly! Here's a sample README file content and title for your GitHub repository:

Title:

Discord Server Player Counter

README Content:

Discord Server Player Counter
This Python script allows you to fetch player data from a game server and send it as a formatted message to a Discord channel using a webhook. It can be used to display real-time player information on a Discord server.

Prerequisites
Python 3.x
requests library (can be installed via pip install requests)
Usage
Clone the repository or download the player_counter.py file.

Open the player_counter.py file in a text editor.

Replace the following placeholders with your actual values:

webhook_url: Replace with your Discord webhook URL.
players_url: Replace with the URL for your game server's player data.
Save the file.

Run the script using the command: python player_counter.py.

The script will start fetching player data from the game server at the specified interval (in seconds) and send it as a formatted message to the specified Discord channel using the webhook.

Customization
You can customize the appearance of the Discord message by modifying the create_embed function in the script. You can change the title, color, and other formatting options according to your preferences.

Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Feel free to update the content based on your specific requirements or preferences. Don't forget to include any additional sections, instructions, or acknowledgments as needed.






