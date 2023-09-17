import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Email server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # This is the appropriate port for Gmail
smtp_username = 'someone@example.com'
smtp_password = 'REDACTED'

# List of recipients and their corresponding image file paths
recipients = [
    {'name': 'Aanchal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Pooja', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Dhruv Mittal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Dampi Ngomdir', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ansh gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kanan', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Arsh Sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Harshita', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kishan kumar mishra', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anshul', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Somaya Modi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shubh Chahal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kush singla', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shaurya Singhal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ansh dubey', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Nitin Dwivedi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Yash Wadhwa', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Utkarsh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Jasman Singh Anand', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Manya', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aniket Tyagi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Pranav Raj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Harshit Tiwari', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rahul kumar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ishaan Deep Rai', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sayali Putcha', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Yasharth Upadhyay', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Deepak gautam', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Gayathri Pasupathi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anant Pratap Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Hari om Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kajal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Pratham Jindal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shivam', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Deepanshu Singla', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Radhika Patidar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anuj Sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Vivek Singh Rathore', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'shubh agarwal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mehdhi Hasan', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mahima Pandey', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Hardik Chhowchharia', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Samarth Goyal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rahul Nayar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Honey', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Manish Pandit', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Krishna Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Tina Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Himanshu', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Krish Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Nimisha Verma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sumit kumar sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rajnish Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Javed Akhtar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'sumith pittala', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Syed Safyan Ali', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rajesh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Devansh Mittal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Chandresh Mirchandani', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Prince Kumar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Avantika Bhardwaj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Suraj kumar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Suryansh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Madhav khandelwal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Tisha Gulati', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aryan Raj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Yashika Chhikara', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Amit Xingh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rohit Bharti', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'AMAN', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shatrughan', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mehar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Tanya Ganguly', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aaryann Handa', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Nitya Ahuja', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Jay Chaurasia', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Divyanshi Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shubham Bajaj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Gaurav Singh Bhandari', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Dakshesh gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Lakshita', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mehak', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anushka Srivastava', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Yashika Mittal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Vidhi wadera', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anuj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Prachi Saha', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Samaira Garg', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Akriti Roy', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aryan Raj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anuj rai', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Devang sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Pratham Rastogi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Diva Parmar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Adwaith Rajesh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mohit Kumar yadav', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Lokesh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Akash Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Naveen verma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rudransh kaushik', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kanak Yadav', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ravi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Harsh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'MANOHARLAL', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Simran Ray', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Vaibhav Kumar Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Amit Kumar Vidyarthi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Devesh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Himanshu Kumar sah', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Krishna', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shruti Verma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Jatin bhardwaj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rahul', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Daksh Sehgal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aditi Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Bhavya', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Dhruv Kumar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sneha Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Chandrashekhar Lodhi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sonu Verma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Manish', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Nikhil Tandon', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Siddharth Malhotra', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Aryan Kapoor', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ishita Verma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kajal Kumari', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kundan', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mohamed farooq m', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Maitri Jain', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Gaurav Mishra', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Kumkum', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anukriti', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Shivam', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sumit Kumar Yadav', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Rajneesh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Parth Rajpoot', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sarthak chadha', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Manav kashya', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Abhinav Dubey', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Devansh Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Abhinav kalra', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Nikunj Goyal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Manav Nagi', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Dhruv Munjal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anukriti Uniyal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Adarsh Singh', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Yash', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Anshika Sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Harsh Jangid', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Sumit', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Vivek Pal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Mini sharma', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Urooba Anwar', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Keshav mittal', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Jasleen kaur', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Amit Raj', 'email': 'someone@example.com', 'image_path': '1.png'},
{'name': 'Ujjwal Gupta', 'email': 'someone@example.com', 'image_path': '1.png'},
]

# Create a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Iterate through the list of recipients and send emails with images
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = recipient['email']
    msg['Subject'] = "Get Ready to Rock Summit'23 with Bhanu Pathak! 🎤"

    # Create a text message part
    text = f"""Hey {recipient['name']},

We hope you're as stoked as we are for the upcoming speaker session featuring none other than the social media sensation Bhanu Pathak, boasting a whopping 1.5M+ followers!

Details at a glance:

🗓️Date: 18th September (Monday)
🕤 Time: 9:30 am
📍 Venue: Seminar Hall 1

Here's a little insider tip: entry will be on a first-come, first-served basis! So, let's kickstart this summit with a bang - make sure you're there early to snag your spot and avoid any last-minute hustle.

Get ready to be inspired, learn, and connect with fellow enthusiasts. This session promises to be nothing short of amazing!

See you bright and early,

Team FIC"""
    
    msg.attach(MIMEText(text, 'plain'))

    # Attach the image
    image_path = recipient['image_path']
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name=image_path)
        msg.attach(image)

    # Send the email
    server.sendmail(smtp_username, recipient['email'], msg.as_string())

# Close the SMTP server connection
server.quit()
