import getpass4
# hard-coding an initial value for pin. It will change after reset.
pin = '7860'

def pin_reset():
    # variable is assigned predefined value of Mother's maiden name, variable 'attempts' is initialized as 0
    # new_pin is assigned value from outer scope variable 'pin', boolean done is initialized as False and
    # reset_trials keeps count of how many times the confirming password has mismatched it is initialized as 0
    mm_name = 'Shree'
    attempts = 0
    new_pin = pin
    done = False
    reset_trials = 0

    # informs user that their pin is blocked, and they should answer security question to reset it
    print('Your PIN is temporarily blocked. \nAnswer security question to reset PIN:'
          ' What is your mother\'s maiden name?')
    # the getpass() method discreetly gets answer to security question from user
    answer = getpass4.getpass(prompt='Answer: ')

    # if answer is correct user is asked to enter new pin and confirm repeatedly until the two entries match
    if answer == mm_name:
        while not done:
            new_pin = getpass4.getpass("Enter new PIN: ")
            if not new_pin.isnumeric() or len(new_pin) != 4:
                reset_trials += 1
                print("User PIN is exactly four digits long, no characters.")
                if reset_trials == 3:
                    done = True
                    print("PIN blocked. Contact customer service.")
                continue
            confirm_pwd = getpass4.getpass("Confirm new PIN: ")
            reset_trials += 1
            if confirm_pwd != new_pin:
                print("PINs don't match. Try again.")
                continue
            if confirm_pwd == new_pin:
                print("PIN successfully changed.")
                attempts = 3
                done = True
            elif reset_trials == 3:
                done = True
                print("Too many failed attempts. Contact customer service or visit our bank branch.")
    else:
        print("PIN blocked. Contact customer service.")
    return new_pin, attempts


# main code
attempts_left = 3
# while loop runs three times
while attempts_left:
    # getpass() gets user input discreetly
    supplied_pin = getpass4.getpass(prompt='Enter your PIN to access baking: ')
    # numeric and length test should also be done in the reset module - work on it
    if not supplied_pin.isnumeric() or len(supplied_pin) != 4:
        attempts_left -= 1
        if attempts_left == 0:
            print("PIN Blocked.")
            pin, attempts_left = pin_reset()
        else:
            print(f"{attempts_left} attempt(s) left. User PIN is exactly four digits long, no characters.")
        continue

    if supplied_pin == pin:
        print('Success!')
        break

    else:
        print(f"Incorrect PIN\n {attempts_left - 1} attempt(s) left!")
        attempts_left -= 1
        if attempts_left == 0:
            pin, attempts_left = pin_reset()
            # above line of code calls function pin_reset() which is defined prior to main code
