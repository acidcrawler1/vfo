# import smtplib

# from email.mime.text import MIMEText

class SendEmail(object):
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send_email(self, user, pwd):
        import smtplib
        gmail_user = user
        gmail_pass = pwd
        FROM = user
        TO = self.recipient if type(self.recipient) is list else [self.recipient]
        SUBJECT = self.subject
        TEXT = self.body

        message = """From: {}\nTo: {}\nSubject: {}\n\n{}""".format(FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pass)
            server.sendmail(FROM, TO, message)
            server.close()
            print("Email sent successfully")
        except Exception as e:
            print(e, "\nFailed to send email")

if __name__ == '__main__':
    my_email = SendEmail('acidcrawler@mail.com', 'Testing', 'Fästing')
    print (my_email)


    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    # smtpserver.login('acidcrawler111@gmail.com', 'pass')
    # https://myaccount.google.com/apppasswords