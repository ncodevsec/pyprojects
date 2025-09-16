import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv() # It loads the .env file

# -------[ Email Content ]-------
# Address
sender = os.environ.get("SENDER")
receiver = os.environ.get("RECEIVER")

# Content
subject = "Automailer - Test Mail"
# Collecting body content from a html file.
body = open("mail-body.html", encoding="utf-8").read() 

# -------[ Create MIMEText Obj ]-------
msg = MIMEText(body, "html") # If body is in plain-text, use "plain"
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject

# -------[ SMTP Setup ]-------
try:
    # Connect to Gmail SMTP Server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() #It secures the connection

    # Login with Gmail (use App Password if 2FA is on)
    server.login(sender, os.environ.get("APP_PASSWORD"))

    # Send email
    server.sendmail(sender, receiver, msg.as_string())

except Exception as e:
    print("Error : ",e) # Prints Errors

finally:
    server.quit() # Quits Server