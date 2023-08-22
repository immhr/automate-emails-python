from smtplib import SMTP

sender = "mihirprasad75@gmail.com"

receivers = ['mipr20ec@cmrit.ac.in',
             'rinaprasad11@gmail.com',
             'mihirprasad75@gmail.com',
             'radhe.prasad@gmail.com']

message = '''From: {}
To: {}
Subject: SMTP e-mail test
Hello,

This is a python generated e-mail message.
Please do not respond.

With Regards
Mihir Prasad'''.format(sender, receivers)

SmtpObject = SMTP('smtp.gmail.com', 25)

SmtpObject.ehlo()
SmtpObject.starttls()
SmtpObject.login(user='mihirprasad75@gmail.com', password='pfznzyutozzhkuuc')

SmtpObject.sendmail(sender, receivers, message)
print("Successfully sent e-mail")
SmtpObject.quit()
