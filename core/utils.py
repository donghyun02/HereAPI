import smtplib
from email.mime.text import MIMEText


def send_email(subject, content, email):
    message = MIMEText(content)
    message['Subject'] = subject

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('reservationfromhere@gmail.com', 'quncfvtlxipktrmf')
    smtp.sendmail('reservationfromhere@gmail.com', email, message.as_string())
    smtp.quit()
