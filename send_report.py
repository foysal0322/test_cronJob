import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Open a URL
url = "https://www.example.com"
driver.get(url)

# Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1351086319815888916/GkSxw4XAuJDCeshqZ95GBLYiwwgk7VCv3LFL7qDsPBIqXebwBshikJd8HcJm-9OT0H6B"

# Send URL to Discord
data = {"content": f"Visited URL: {driver.current_url}"}
requests.post(DISCORD_WEBHOOK_URL, json=data)

# Close the browser
driver.quit()
