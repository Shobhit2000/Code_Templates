from otp import send_OTP, check_OTP, new_acc_notification, updates

otp = send_OTP("8240524439")
n = input()
bool = check_OTP(otp, n)

if bool == 1: print("verified")
else: print("wrong otp")
#
# status_new = new_acc_notification('enter mobile numbers')
#
# status_updates = updates('mobile number, text message')
