
import smtplib
from smtplib import SMTP
email = 'chahat.7874@gmail.com'
password = 'ilovegmail1211'

from_mail = email
#
def sendmail(subject, message, to_mail):    
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login(email, password)
	message = f'Subject : {subject} \n\n {message}'
	#s.sendmail(from_mail, to_mail, msg.as_string())
	s.sendmail(from_mail, to_mail, message)
	s.quit()




# import smtplib

# sender = 'chahat.7874@gmail.com'
# receivers = ['to@todomain.com']

# message = """From: From Person <chahat.7874@gmail.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """

# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)         
#    print "Successfully sent email"
# except SMTPException:
#    print "Error: unable to send email"