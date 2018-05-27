import smtplib

from datetime import datetime

from email.MIMEMultipart import MIMEMultipart

from email.MIMEText import MIMEText

fromaddr = "prateekagrawal89760@gmail.com"

toaddr = "dmadnawat.43@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Motion Alert"

body = 'A motion has been detected.\nTime: %s' % str(datetime.now())

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(fromaddr, "sciencesciences8307")

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()


