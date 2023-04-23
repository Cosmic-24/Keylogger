import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail(filename):

    # Email Information Part
    sender_address = "Enter Senders Email Address"
    sender_password = "Enter Senders Password"
    receiver_address = "Enter Receivers Email Address"
    subject = "Add Subject If Required"
    body = "Add Body if Required"
    attachment = open(filename, "rb")

    # Create Attachment for Mail
    attach = MIMEBase("application", "octet-stream")
    attach.set_payload(attachment.read())
    encoders.encode_base64(attach)
    attach.add_header('Content-Disposition','attachment; filename= %s' % filename)

    # Create Body of mail using multipart and convert it to string
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    message.attach(MIMEText(body, "plain"))
    message.attach(attach)
    text = message.as_string()

    # Send mail using the smtp protocol
    send = smtplib.SMTP('smtp.gmail.com', 587)
    send.starttls()
    send.login(sender_address, sender_password)
    send.sendmail(sender_address, receiver_address, text)
    send.quit()
