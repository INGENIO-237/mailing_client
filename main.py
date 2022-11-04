import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmsil.com', 25)

server.ehlo()

user = 'ingeniokhalif@gmail.com'

with open('password.txt', 'r') as f:
    password = f.read()

server.login(user, password)

msg = MIMEMultipart()
msg['From'] = user
msg['To'] = 'ingeniokhalif@gmail.com'
msg['Subject'] = 'Mail sending test'

with open('messages.txt', 'r') as f:
    content = f.read()

msg.attach(MIMEText(content, 'plain'))

filename = 'geek.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail(user, msg['To'], text)