import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, unique_link, discord_id):
    subject = "Your Unique Discord Verification Link"
    body = f"Hey there, {discord_id}! /nWe're excited to have you at HackCUNY! You have been selected to participate in HackCUNY 2024! /nPlease click the following link to verify your Discord account and enter the verified channel: {unique_link} "
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()

# for discord_id, info in users_data.items():
#     send_email("your_email@gmail.com", "your_password", info['email'], unique_links[discord_id])


# verify@hackcuny.com