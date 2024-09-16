#Importing the required libraries
import smtplib
from email.message import EmailMessage
import random

#Taking input from the user
name = input("Enter your name\n")
sender_mail_id = input("\nEnter the mail ID to send OTP\n")

#Generating OTP using randrange from random library.
otp = str(random.randrange(100000, 999999))

#Username and password of your e-mail address.
username = "kabilantestmail@gmail.com"
password = "shgp ehzn sjhx ushv"

#Sending the OTP to the user's mail id.
msg = EmailMessage()
msg['Subject'] = 'OTP Verification Mail' #Email - Subject
msg['From'] = username #Email - From
msg['To'] = sender_mail_id  #Email - To
msg.set_content(f'Hi 👋 {name},\n\nPlease find the OTP for Verification : {otp}\n\nThanks !!!') #Email - Body

#Logging In to your e-mail address using smtp via SSL(Secure Sockets Layer) for Security.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #Using Gmail's Host and Port number
    smtp.login(username, password)
    smtp.send_message(msg)

#Acknowledgement message
print(f"\nOTP Sent to : {sender_mail_id} \n")

#Function to verify the OTP by giving 3 Chances to enter OTP.
def verify_otp(otp_1):
    if otp_1 == otp:
        print("\nCorrect OTP 😀... \nVerification Successfull !!!\n")
    else:
        n = 2
        print(f"\nYou have entered Incorrect OTP ☹️, You have {n} more chances to enter the Correct OTP\n")
        while(n!=0):
            otp_1 = input("Please Correctly re-enter the OTP received\n")
            if otp_1 == otp:
                print("\nCorrect OTP 😀... \nVerification Successfull !!!\n")
                break
            else:
                n = n-1
                print(f"\nYou have entered Incorrect OTP ☹️, You have {n} more chances to enter the Correct OTP\n")
                if n == 0:
                  print("Hard Luck ☹️! Please try again to geneate another OTP...")

#Asking User to enter the OTP received.
otp_1 = input("Enter the OTP received\n")

#Calling the Verify_otp function by the input.
verify_otp(otp_1)