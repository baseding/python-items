import smtplib

def mailx(message='message empty'):
    'Send mail function'

    SERVER = "mail.10690007.net"
    FROM = "manager1@10690007.net"
    TO = ["yfding@mail.etonenet.com"]                        # must be a list
    SUBJECT = "Website access time Alert"
    TEXT = message

    # Prepare actual message
    # Notice: Can not use blank before FROM:,TO,Subject etc.
    message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    try:
        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()
    except smtplib.SMTPException:
        print("mail send failed")

