# Write a python programme that can
# Check a PIN
# Keep taking input from keyboard until it is identical to PIN
# Restrict number to 3 attempts (keep as var)
# Then output suitable message for success / failure
# Include number of attempts in message

# import getpass  # needs to be run in debug mode

Attempts = 3
correct_PIN = 1234

while Attempts != 0:  # executes code block while attempts are not equal to 0
    supplied_pin = int(input("Please enter your PIN: "))
    if supplied_pin != correct_PIN:
        Attempts -= 1   # if attempts are less than or equal to 1
        print(f"Incorrect PIN, You have {Attempts} Attempts left")
    else:
        print("Kaching")
        break
        # if pin is correct, terminal prints kaching then break will end while loop

