# Author: Melis Luca <melis.luca2014@gmail.com>
# 3-Parts: smtplib

# Required:
# Enable "unsecure apps" in Gmail to use this.
# Install "smtplib" library

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR GOOGLE MAIL", "YOUR PASSWORD") 

msg = "Hi, this is a mail sent using Python!"  
server.sendmail('SENDER-MAIL CCN', "RECEIVER_MAIL", msg)

server.quit()
