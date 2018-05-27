import os

import smtplib

from email.MIMEMultipart import MIMEMultipart

from email.MIMEText import MIMEText

from email.MIMEBase import MIMEBase

from email import encoders

def sendfile(folder_location):
    fromaddr = "prateekagrawal89760@gmail.com"

    toaddr = "mudit23june@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Motion was detected"

    body = "Video of Motion Detected"

    msg.attach(MIMEText(body, 'plain'))

    rootpath = folder_location

    filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]

    filelist = [f for f in filelist if os.path.isfile(f)]

    newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

    filename = newest

    rootpath = folder_location

    filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]

    filelist = [f for f in filelist if os.path.isfile(f)]

    newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

    attachment = open(newest, "rb")

    part = MIMEBase('application', 'octet-stream')

    part.set_payload((attachment).read())

    encoders.encode_base64(part)

    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(fromaddr, "sciencesciences8307")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)

    server.quit()


