import smtplib
import ssl
import os
from dotenv import load_dotenv


# Function to send an email using Gmail SMTP
def send_email(message):
    # Gmail SMTP server details
    host = "smtp.gmail.com"
    port = 465

    # Sender's Gmail account credentials
    username = "arifdiu2@gmail.com"

    # Load app password from environment variables
    load_dotenv()
    password = os.getenv("PASSWORD")

    # Receiver's email address
    receiver = "arifdiu2@gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Convert the message to bytes using UTF-8 encoding
    message = message.encode('utf-8')

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Login to the sender's Gmail account
        server.login(username, password)

        # Send the email from the sender to the receiver
        server.sendmail(username, receiver, message)