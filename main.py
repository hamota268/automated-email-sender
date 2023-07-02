import smtplib
import time

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Gmail configuration
        if "gmail.com" in sender_email:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
        # ProtonMail configuration
        elif "protonmail.com" in sender_email:
            smtp_server = 'smtp.protonmail.com'
            smtp_port = 587
        else:
            print("Unsupported email provider.")
            return

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            email_body = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_body)

        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your credentials.")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

# User inputs
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
receiver_email = input("Enter the recipient's email address: ")
subject = input("Enter the email subject: ")
message = input("Enter the email message: ")
delay_time = int(input("Enter the delay time (in seconds): "))

# Delay before sending the email
time.sleep(delay_time)

# Send email
send_email(sender_email, sender_password, receiver_email, subject, message)
