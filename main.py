import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# Define the topic for the news search
topic = "tesla"

# Construct the URL for the News API request using the API key
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "language=en&"
       "apiKey=") + api_key

# Make a GET request to the News API
request = requests.get(url)

# Parse the response content as JSON
content = request.json()

# Email body message with subject line
message = "Subject: Today's News" + "\n"

# Iterate through each article received from the API (limiting to the first
# 15 articles)
for article in content["articles"][:15]:
    if article["title"] is not None:
        # Extract the title, description and url of the article and append
        # to the message
        title = article["title"]
        description = article["description"]
        article_url = article["url"]
        message += f"{title}\nDescription: {description}\n{article_url}\n\n"

# Send the email with all titles and descriptions as the message
send_email(message)
