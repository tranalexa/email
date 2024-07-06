import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_content import email_template

# Example usage:
sender_email = "senderemail@gmail.com"

# Function to send HTML email with image
def send_email(sender_email, sender_name, recipient_email, recipient_name, organization):
    # Setup the email
    message = MIMEMultipart()
    message['From'] = f"{sender_name} <{sender_email}>"
    message['To'] = recipient_email
    message['Subject'] = "2025 Stanford Asian American Awards Call for Nominations"
    
    # Fill the message body with HTML content
    email_content = email_template.format(recipient_name=recipient_name, sender_name=sender_name, organization=organization, sender_name_2=sender_name)
    message.attach(MIMEText(email_content, 'html'))

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server details
    smtp_server.starttls()
    smtp_server.login(sender_email, "PASSWORD")  # Replace with your email login

    # Send email
    smtp_server.sendmail(sender_email, recipient_email, message.as_string())

    # Disconnect from the SMTP server
    smtp_server.quit()


# Reading recipients from a CSV file
with open('recipients.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        recipient_name = row['recipient_name']
        recipient_email = row['recipient_email']
        sender_name = row['sender_name']
        organization = row['organization']
        send_email(sender_email, sender_name, recipient_email, recipient_name, organization)
        print(f"Email sent to {recipient_name} at {recipient_email} from {sender_name}")