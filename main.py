import smtplib
from email.message import EmailMessage
import random
from otp import nums, user_email_id, user_pwd  #the file should be in the same directory

email_input = input("Enter Email ID:")         #send the otp to this email
otp = str(random.choice(nums))

usr_mail = user_email_id
usr_pwd = user_pwd

msg = EmailMessage()
msg['Subject'] = 'OTP Verification For Company Name Login'
msg['From'] = usr_mail
msg['To'] = email_input
msg.set_content(otp)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # for gmail, for yahoo,outlook etc check smtp docs or google
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(usr_mail, usr_pwd)

    smtp.send_message(msg)

print("Enter OTP sent to the email ID:")
num_input = input()
if num_input == otp:                            #if otp matches then "do something"
    print("Successfull!")                      
else:
    print("Unsuccessfull Attempt , Try Again:") #if not then "do something else"
