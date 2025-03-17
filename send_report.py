import requests

url = "https://api.restful-api.dev/objects"
message = requests.request("GET", url)

# Discord Webhook URL (Replace with your webhook)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1351086319815888916/GkSxw4XAuJDCeshqZ95GBLYiwwgk7VCv3LFL7qDsPBIqXebwBshikJd8HcJm-9OT0H6B"

data = {"content": str(message.text)}
response = requests.post(DISCORD_WEBHOOK_URL, json=data)




# Example Usage



