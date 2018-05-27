import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print(s.getsockname()[0])x = s.getsockname()[0]s.close()

import smtplib

from email.MIMEMultipart import MIMEMultipart

from email.MIMEText import MIMEText

fromaddr = "prateekagrawal89760@gmail.com"

toaddr = ""

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Motion Detected"

body = xmsg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(fromaddr, "sciencesciences8307")

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()


