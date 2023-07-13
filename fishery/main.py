import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor

# Email configuration
smtp_host = 'smtp-mail.outlook.com'
smtp_port = 587
sender_email = 'someone@example.com'
sender_password = 'REDACTED'

def send_email(receiver_email):
    # Create the multipart message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Get Canva Pro by Joining the Team'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Load and attach the HTML content
    with open('email_template.html', 'r') as file:
        html_content = file.read()

    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Send the email
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return f"{receiver_email} done!"
    except Exception as e:
        return f"{receiver_email} not available!\n{e}"

# List of email recipients
recipients = []

for roll in ('171','172','181','131','132','136','831','135','145','120','105','821','836','838','820','121'):
    for num in range(1, 10):
        receiver_email = f'{roll}0{num}@arsd.du.ac.in'
        recipients.append(receiver_email)
    for num in range(10, 100):
        receiver_email = f'{roll}{num}@arsd.du.ac.in'
        recipients.append(receiver_email)

# Send emails in parallel
with ThreadPoolExecutor() as executor:
    results = executor.map(send_email, recipients)

# Print the results
for result in results:
    print(result)
