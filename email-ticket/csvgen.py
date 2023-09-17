import csv

csv_data = """Aanchal,someone@example.com,1.png
Pooja,someone@example.com,1.png
Dhruv Mittal,someone@example.com,1.png
Dampi Ngomdir,someone@example.com,1.png
Ansh gupta,someone@example.com,1.png
Kanan,someone@example.com,1.png
Arsh Sharma,someone@example.com,1.png
Harshita,someone@example.com,1.png
Kishan kumar mishra,someone@example.com,1.png
Anshul,someone@example.com,1.png
Somaya Modi,someone@example.com,1.png
Shubh Chahal,someone@example.com,1.png
Kush singla,someone@example.com,1.png
Shaurya Singhal,someone@example.com,1.png
Ansh dubey,someone@example.com,1.png
Nitin Dwivedi,someone@example.com,1.png
Yash Wadhwa,someone@example.com,1.png
Utkarsh,someone@example.com,1.png
Jasman Singh Anand,someone@example.com,1.png
Manya,someone@example.com,1.png
Aniket Tyagi,someone@example.com,1.png
Pranav Raj,someone@example.com,1.png
Harshit Tiwari,someone@example.com,1.png
Rahul kumar,someone@example.com,1.png
Ishaan Deep Rai,someone@example.com,1.png
Sayali Putcha,someone@example.com,1.png
Yasharth Upadhyay,someone@example.com,1.png
Deepak gautam,someone@example.com,1.png
Gayathri Pasupathi,someone@example.com,1.png
Anant Pratap Singh,someone@example.com,1.png
Hari om Singh,someone@example.com,1.png
Kajal,someone@example.com,1.png
Pratham Jindal,someone@example.com,1.png
Shivam,someone@example.com,1.png
Deepanshu Singla,someone@example.com,1.png
Radhika Patidar,someone@example.com,1.png
Anuj Sharma,someone@example.com,1.png
Vivek Singh Rathore,someone@example.com,1.png
shubh agarwal,someone@example.com,1.png
Mehdhi Hasan,someone@example.com,1.png
Mahima Pandey,someone@example.com,1.png
Hardik Chhowchharia,someone@example.com,1.png
Samarth Goyal,someone@example.com,1.png
Rahul Nayar,someone@example.com,1.png
Honey,someone@example.com,1.png
Manish Pandit,someone@example.com,1.png
Krishna Gupta,someone@example.com,1.png
Tina Gupta,someone@example.com,1.png
Himanshu,someone@example.com,1.png
Krish Gupta,someone@example.com,1.png
Nimisha Verma,someone@example.com,1.png
Sumit kumar sharma,someone@example.com,1.png
Rajnish Singh,someone@example.com,1.png
Javed Akhtar,someone@example.com,1.png
sumith pittala,someone@example.com,1.png
Syed Safyan Ali,someone@example.com,1.png
Rajesh,someone@example.com,1.png
Devansh Mittal,someone@example.com,1.png
Chandresh Mirchandani,someone@example.com,1.png
Prince Kumar,someone@example.com,1.png
Avantika Bhardwaj,someone@example.com,1.png
Suraj kumar,someone@example.com,1.png
Suryansh,someone@example.com,1.png
Madhav khandelwal,someone@example.com,1.png
Tisha Gulati,someone@example.com,1.png
Aryan Raj,someone@example.com,1.png
Yashika Chhikara,someone@example.com,1.png
Amit Xingh,someone@example.com,1.png
Rohit Bharti,someone@example.com,1.png
AMAN,someone@example.com,1.png
Shatrughan,someone@example.com,1.png
Mehar,someone@example.com,1.png
Tanya Ganguly,someone@example.com,1.png
Aaryann Handa,someone@example.com,1.png
Nitya Ahuja,someone@example.com,1.png
Jay Chaurasia,someone@example.com,1.png
Divyanshi Gupta,someone@example.com,1.png
Shubham Bajaj,someone@example.com,1.png
Gaurav Singh Bhandari,someone@example.com,1.png
Dakshesh gupta,someone@example.com,1.png
Lakshita,someone@example.com,1.png
Mehak,someone@example.com,1.png
Anushka Srivastava,someone@example.com,1.png
Yashika Mittal,someone@example.com,1.png
Vidhi wadera,someone@example.com,1.png
Anuj,someone@example.com,1.png
Prachi Saha,someone@example.com,1.png
Samaira Garg,someone@example.com,1.png
Akriti Roy,someone@example.com,1.png
Aryan Raj,someone@example.com,1.png
Anuj rai,someone@example.com,1.png
Devang sharma,someone@example.com,1.png
Pratham Rastogi,someone@example.com,1.png
Diva Parmar,someone@example.com,1.png
Adwaith Rajesh,someone@example.com,1.png
Mohit Kumar yadav,someone@example.com,1.png
Lokesh,someone@example.com,1.png
Akash Singh,someone@example.com,1.png
Naveen verma,someone@example.com,1.png
Rudransh kaushik,someone@example.com,1.png
Kanak Yadav,someone@example.com,1.png
Ravi,someone@example.com,1.png
Harsh,someone@example.com,1.png
MANOHARLAL,someone@example.com,1.png
Simran Ray,someone@example.com,1.png
Vaibhav Kumar Singh,someone@example.com,1.png
Amit Kumar Vidyarthi,someone@example.com,1.png
Devesh,someone@example.com,1.png
Himanshu Kumar sah,someone@example.com,1.png
Krishna,someone@example.com,1.png
Shruti Verma,someone@example.com,1.png
Jatin bhardwaj,someone@example.com,1.png
Rahul,someone@example.com,1.png
Daksh Sehgal,someone@example.com,1.png
Aditi Singh,someone@example.com,1.png
Bhavya,someone@example.com,1.png
Dhruv Kumar,someone@example.com,1.png
Sneha Singh,someone@example.com,1.png
Chandrashekhar Lodhi,someone@example.com,1.png
Sonu Verma,someone@example.com,1.png
Manish,someone@example.com,1.png
Nikhil Tandon,someone@example.com,1.png
Siddharth Malhotra,someone@example.com,1.png
Aryan Kapoor,someone@example.com,1.png
Ishita Verma,someone@example.com,1.png
Kajal Kumari,someone@example.com,1.png
Kundan,someone@example.com,1.png
Mohamed farooq m,someone@example.com,1.png
Maitri Jain,someone@example.com,1.png
Gaurav Mishra,someone@example.com,1.png
Kumkum,someone@example.com,1.png
Anukriti,someone@example.com,1.png
Shivam,someone@example.com,1.png
Sumit Kumar Yadav,someone@example.com,1.png
Rajneesh,someone@example.com,1.png
Parth Rajpoot,someone@example.com,1.png
Sarthak chadha,someone@example.com,1.png
Manav kashya,someone@example.com,1.png
Abhinav Dubey,someone@example.com,1.png
Devansh Gupta,someone@example.com,1.png
Abhinav kalra,someone@example.com,1.png
Nikunj Goyal,someone@example.com,1.png
Manav Nagi,someone@example.com,1.png
Dhruv Munjal,someone@example.com,1.png
Anukriti Uniyal,someone@example.com,1.png
Adarsh Singh,someone@example.com,1.png
Yash,someone@example.com,1.png
Anshika Sharma,someone@example.com,1.png
Harsh Jangid,someone@example.com,1.png
Sumit,someone@example.com,1.png
Vivek Pal,someone@example.com,1.png
Mini sharma,someone@example.com,1.png
Urooba Anwar,someone@example.com,1.png
Keshav mittal,someone@example.com,1.png
Jasleen kaur,someone@example.com,1.png
Amit Raj,someone@example.com,1.png
Ujjwal Gupta,someone@example.com,1.png"""

# Split the CSV data into lines
csv_lines = csv_data.strip().split('\n')

# Initialize an empty list to store the dictionaries
recipients = []

# Loop through the CSV lines and create dictionaries
for line in csv_lines:
    name, email, image_path = line.split(',')
    recipient = {'name': name, 'email': email, 'image_path': image_path}
    recipients.append(recipient)

# Print the list of dictionaries
for recipient in recipients:
    print(str(recipient)+',')
