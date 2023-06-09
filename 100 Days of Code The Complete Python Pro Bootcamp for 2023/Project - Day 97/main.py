import smtplib

import datetime

import os



def send_email(sender_email, sender_password, receiver_email, subject, message):

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)



        msg = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender_email, receiver_email, msg)

        print("Email sent successfully!")



        server.quit()

    except Exception as e:

        print("An error occurred while sending the email:", str(e))





def automate_daily_reminder():

    # Set up email credentials

    sender_email = "your_email@gmail.com"  # Replace with your sender email

    sender_password = "your_password"  # Replace with your sender email password

    receiver_email = "recipient_email@gmail.com"  # Replace with the recipient email

    subject = "Daily Reminder"

    message = "Don't forget to complete your daily tasks!"



    # Get the current date

    current_date = datetime.date.today()



    # Check if a file exists for the current date

    file_name = f"{current_date}.txt"

    if os.path.isfile(file_name):

        # Email reminder already sent for today

        print("Reminder already sent for today.")

    else:

        # Send the email reminder

        send_email(sender_email, sender_password, receiver_email, subject, message)



        # Create a file to mark the reminder as sent

        with open(file_name, "w") as file:

            pass





# Run the automation function

automate_daily_reminder()

