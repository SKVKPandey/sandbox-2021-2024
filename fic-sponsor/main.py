import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "skvkpandey@gmail.com"
receiver_emails = ['someone@example.com']
subject = "Sponsorship Invitation for Finance Summit '23"
html_content = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap">
    <style>
        /* Global styles */
        body {
            font-family: 'Montserrat', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .subheading {
            display: flex;
            flex-direction: row;
            justify-content: center;
        }
        .container {
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        .logo-left,
        .logo-right {
            position: absolute;
            top: 20px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .logo-left img,
        .logo-right img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .logo-right {
            position: absolute;
            top: 20px;
            right: 20px;
        }
        .logo-left {
            position: absolute;
            top: 20px;
            left: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .college-name {
            font-size: 2rem; /* Adjust the font size as needed */
            font-weight: bold;
            margin-top: 10px;
        }
        .subheading {
            font-size: 1rem; /* Adjust the font size as needed */
            color: #888;
            margin-bottom: 10px;
        }

        /* Navigation styles */
        .navigation {
            text-align: center;
            margin-top: 20px;
        }

        .navigation a {
            color: #007bff;
            text-decoration: none;
            margin: 0 10px;
        }

        /* CTA button styles */
        .cta-button {
            display: block;
            width: 100%;
            text-align: center;
            margin: 30px 0;
        }

        .cta-button a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #ffffff;
            text-decoration: none;
            border-radius: 5px;
        }
        .navigation img {
            width: 30px;
            height: auto;
        }

        /* Responsive media queries */
        @media (min-width: 768px) {
            /* Styles for screens wider than 768px (desktop) */
            .container {
                max-width: 700px;
            }
        }

        @media (max-width: 767px) {
            /* Styles for screens up to 767px (mobile) */
            .container {
                max-width: 100%;
                padding: 10px;
            }
            .college-name {
                font-size: 1.5rem; /* Adjust the font size as needed */
            }
            .subheading {
                font-size: 0.8rem; /* Adjust the font size as needed */
            }
            .logo-left, .logo-right {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="subheading">
                <div class="logo-left">
                    <img src="https://i.ibb.co/M1CXB9R/1-2.png" alt="ARSD College" border="0">
                </div>
                <div>
                    Atma Ram Sanatan Dharma College
                    <br>
                    Under the aegis of IQAC &amp;
                    <br>
                    दिल्ली विश्वविद्यालय | UNIVERSITY OF DELHI
                    <br>
                    ACCREDITED GRADE 'A++' BY NAAC (CGPA 3.77/4.00)
                    <br>
                    The Finance &amp; Investment Cell (FIC)
                    <br>
                    ALL INDIA 6th RANK BY NIRF (MoE)
                    <br>
                    आत्मा राम सनातन धर्म महाविद्यालय
                </div>
                <div class="logo-right">
                    <img src="https://i.ibb.co/GxNNFpx/2-4.png" alt="FIC ARSD" border="0">
                </div>
            </div>
            <div class="college-name">Finance Summit '23</div>
            <div class="navigation" style="font-size: 50px; color: #aaa;"> 
                <a href="https://www.instagram.com/ficarsd/"><img src="https://i.ibb.co/V3XcTVK/insta.png" alt="insta" border="0"></a> |
                <a href="https://www.linkedin.com/company/fic-arsd/"><img src="https://i.ibb.co/H72vrDK/lkd.png" alt="lkd" border="0"></a> |
                <a href="https://www.facebook.com/ficarsd?mibextid=ZbWKwL"><img src="https://i.ibb.co/mBx4t7H/fb.png" alt="fb" border="0"></a>
            </div>
        </div>
        <div class="body-content">
            <p>Dear Sir/Ma'am,</p>
            <p>I am writing to invite you to become a sponsor for the upcoming <strong>Finance Summit '23</strong> organized by the Finance and Investment Cell of <em>ARSD College, University of Delhi</em> (6th as per college rankings in NIRF framework, highest accredited college as per NAAC in India) due to be held in <strong>Mid - September</strong>.</p>

            <h2>Event Overview:</h2>
            <p>The Finance Summit is a prestigious event that brings together finance societies from various colleges across Delhi for a day of insightful discussions, competitions, and networking opportunities. This year's summit promises to be bigger and better than ever before, and we believe your partnership would be invaluable in making it a grand success.</p>

            <h2>Event Highlights:</h2>
            <ul>
                <li><strong>Speaker Session:</strong> Notable speakers with a vast social media following (Over 1 million followers) will share their experiences and insights, providing attendees with valuable knowledge and inspiration.</li>
                <li><strong>Finance Challenge:</strong> A competitive event designed to test participants' financial knowledge, analytical skills, and problem-solving abilities.</li>
            </ul>

            <h2>Sponsorship Categories (Open to alterations according to the brand's objectives):</h2>
            <ol>
                <li>Title Sponsor for Summit</li>
                <li>Associate Sponsors for Competitions</li>
                <li>Food/Gifting Partners</li>
                <li>Beverages Partner</li>
                <li>Education Partner</li>
                <li>Finance Partner</li>
                <li>Printing Partner</li>
                <li>General Sponsors</li>
            </ol>

            <h2>Benefits to Sponsors:</h2>
            <ul>
                <li>Access to a highly engaged audience comprising finance enthusiasts, students, and professionals.</li>
                <li>Specific posts for the brand and logos on all promotional posts on various social media apps. (Instagram - 1.9k followers, Linkedin - 1k+ followers)</li>
                <li>Promotion through media partners reaching over 1 lakh students.</li>
                <li>Message forwards in multiple WhatsApp groups of different colleges.</li>
                <li>Offline marketing through posters and banners inside ARSD campus, student hubs like Satya Niketan and nearby colleges.</li>
                <li>Multiple shoutouts throughout the event.</li>
            </ul>

            <p>We believe that your esteemed organization's support as a sponsor will significantly contribute to the success of the Finance Summit and enrich the experiences of all attendees. We are open to discussing the sponsorship packages in detail and tailoring them to suit your specific marketing objectives.</p>
        </div>
        <div class="cta-button">
            <a href="http://wa.me/+919106804743">Become a Sponsor</a>
        </div>
        <div class="testimonials">
            <!-- Testimonials or Past Successes section can go here -->
        </div>
        <div class="contact-info">
            <!-- Contact Information section can go here -->
        </div>
        <div class="footer">
            <p>Warm Regards<br/>
            Shashank Kashyap<br/>
            Director of Operations<br/></p>
        </div>
    </div>
</body>
</html>
"""

# Connect to the SMTP server (in this case, Gmail's SMTP server)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Login to your email account
username = "skvkpandey@gmail.com"
password = "REDACTED"

# Create a secure connection to the server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)

    try:

        for receiver_email in receiver_emails:

            # Create a MIME object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach the HTML content to the MIME object
            msg.attach(MIMEText(html_content, 'html'))
            
            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("HTML email sent successfully!")

    except Exception as e:
        print("Error: Unable to send email.")
        print(e)
    
except Exception as e:
    print(e)
    
finally:
    # Close the connection
    server.quit()
