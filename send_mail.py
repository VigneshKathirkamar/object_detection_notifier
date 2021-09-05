from email.mime import multipart
import os 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
# nqfsixstmwaanxwx

username = 'i51vignesh@gmail.com'
password = ''


def send_mail(text="Email body", subject="Hello",from_email= "spacemonkey <i51vignesh@gmail.com>",to_emails=None, html=None,attachment=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    with open(attachment, 'rb') as f:
        img_data = f.read()

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    image = MIMEImage(img_data, name=os.path.basename(attachment))

    # if html != None:
    #     html_part = MIMEText("<h1> This is working </h1>", 'html')
    #     msg.attach(txt_part)
    msg.attach(image)
    msg_str = msg.as_string()
    
    # Attachment details
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit() # quits the server

detect_object_path = '/home/vignesh/virtual_environments/person_notifier/ext_data/detected_objects'

for i in os.listdir(detect_object_path):
    send_mail(to_emails=['i51vignesh@gmail.com'],attachment=detect_object_path+'/'+i)
