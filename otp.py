# program according to Indian Phone Numbers

from twilio.rest import Client
import random
import math

otp = 000000
account_sid = 'AC4985e55ac97ba07f2c3cc21e8ea1a7ef'
auth_token = '6ad6704da57b120d4ea0fb974f85a4bb'
client = Client(account_sid, auth_token)

# notification for new User
def new_acc_notification(n1, n2):   # n1, n2 = numbers of the volunteer and end user
    message = client.messages \
        .create(
        body='Account created !',
        from_='+12056724748',
        to=str("+91" + n1)
    )
    message = client.messages \
        .create(
        body='Account created !',
        from_='+12056724748',
        to=str("+91" + n2)
    )
    return "Sent"

# notification for new schemes
def updates(n, s):                     # n = number, s = text_msg to be sent
    message = client.messages \
        .create(
        body=str(n),
        from_='+12056724748',
        to=str("+91" + n)
    )
    return "Sent"

# for login
def send_OTP(number):           # number = number to send otp on
    global otp
    otp = str(int(math.pow(10, 6) * random.random()))
    message = client.messages \
                    .create(
                         body=str(otp),
                         from_='+12056724748',
                         to=str("+91" + number)
                     )
    return otp

def check_OTP(otp1, en_otp):  # otp1 = initial otp, en_otp = otp entered by the user for verification
    if en_otp == otp1:
        return "Verified"
    else:
        return "Not Verified"
