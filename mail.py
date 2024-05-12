import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my = "visionofus01@gmail.com"
password = "cctkrdxqxkjjqmpg"
re="2k21it63@kiot.ac.in"
msgg=
email_body = msgg
msg = MIMEMultipart('alternative',None,[MIMEText(email_body,'html')])

msg['Subject'] = " Email From Python Pakkva Iruka "
msg['From'] = my
msg['To'] = re

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(my,password)
    server.sendmail(my,re,msg.as_string())
    server.quit()
    print(f'Email Sent:{email_body}')
except:
    print("Error")