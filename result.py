import smtplib # Used for mail 
from email.mime.multipart import MIMEMultipart # When we want to send attachements or alternative text in mail 
from email.mime.text import MIMEText  # Used For Sending text mails
from email.mime.image import MIMEImage
 
my = "visionofus01@gmail.com" # Mailid
password = "cctkrdxqxkjjqmpg" # App Password
re="visionofus01@gmail.com" # Reciver Mail Id


# Mail
mail=['streshi17@gmail.com','2k21it44@kiot.ac.in','2k21it17@kiot.ac.in']
name=['Reshi','Reshi CLg','Fradu']
res=['m3:o , ph2:0','dj;ac,adc;a','fds:A,  DM:O,  Oops:B+,  DPCO:A,  DSA:O']

for i in range(len(mail)):
        re=mail[i]
        n=name[i]
        r=res[i]
        email_body = "Name:"+n+'\n'+"Your Result is: "+r
        msg = MIMEMultipart('alternative',None,[MIMEText(email_body,'html')]) # The Message 
        msg['Subject'] = " Absentees List " #Subject Of Mail
        msg['From'] = my # From Address
        msg['To'] = re # Reciver Address
        try:
                server = smtplib.SMTP('smtp.gmail.com:587') # Connection of mail 
                server.ehlo() #  to identify the domain name of the sending host to SMTP before you issue a MAIL FROM command
                server.starttls() #to inform the email server that the email client wants to upgrade from
                server.login(my,password) # Login
                server.sendmail(my,re,msg.as_string())# Sending mail
                server.quit() # Eding The Connection
                print(f'Email Sent:{email_body}') # Confirmation
        except:
                print("Error") # If Error
print("Succes")