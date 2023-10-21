
''' You can spam your friends with 100 emails'''

# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("email_2@gmail.com", "auth")

for i in range(50):
    # message to be sent
    message = "Enter your message here "+str(i)
    # sending the mail
    s.sendmail("email_2@gmail.com", "email_1@gmail.com", message)

# terminating the session
s.quit()
print("Done")
