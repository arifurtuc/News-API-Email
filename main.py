import requests
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# Construct the URL for the News API request using the API key
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-15&sortBy"
       "=publishedAt&apiKey=") + api_key

# Make a GET request to the News API
request = requests.get(url)

# Parse the response content as JSON
content = request.json()

# Iterate through each article received from the API
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

