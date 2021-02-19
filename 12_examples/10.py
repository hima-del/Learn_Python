import math
import random

def generate_otp():
    digits = "0123456789"
    otp = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp

print(generate_otp())