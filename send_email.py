from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "info@adultteendrivingschool.com"
    from_password = "{_JL1Y-wnSrS"
    to_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s</strong>. Average height is: %s. Based on %s number of people." % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('mail.adultteendrivingschool.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
