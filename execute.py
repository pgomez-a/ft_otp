#############
# Libraries #
#############

import time
import math
import hmac
import sys

#############
# Functions #
#############

def store_key(key):
    try:
        with open(sys.argv[1], "rb") as f:
            key = f.read()
    except:
        print("Error: (open) " + sys.argv[1] + " couldn't be opened")
        return
    try:
        hex_key = int(key, 16)
        hex_key = str(key)
        if len(hex_key) < 64:
            print("./ft_otp: error: key must be 64 hexadecimal characters.")
            return
        with open("./ft_otp.key", "wb") as f:
            f.write(hex_key.encode())
            print("Key was successfully saved in ft_otp.key.")
    except:
        print("./ft_otp: error: key must be 64 hexadecimal characters.")
        return

def create_key(master_key):
    try:
        with open(master_key, "rb") as f:
            master_key = f.read()
    except:
        print("Error: (open) can't obtain master key")
        return
    time_period = str(math.floor(time.time() / 30))
    hmac_sha1 = hmac.new(master_key, time_period.encode(), "sha1")
    hmac_sha1 = hmac_sha1.hexdigest()
    key = hmac_sha1[int(hmac_sha1[39], 16)*2:int(hmac_sha1[39], 16)*2 + 7]
    key += "0"
    key = int(key, 16)
    key = str(key%(10**6))
    if len(key) < 6:
        len_key = len(key)
        for i in range(len_key, 6):
            key += "0"
    print(key)

##################################
# Program: python execute.py S G #
##################################

if sys.argv[1] != "0" and sys.argv[2] != "0":
    print("Error: (format) ./program [-gk]")
    exit(1)

if sys.argv[1] != "0":
    store_key(sys.argv[1])
elif sys.argv[2] != "0":
    create_key(sys.argv[2])
