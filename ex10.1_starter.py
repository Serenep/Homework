Bank_greeting = 'Welcome to the Bank of Mum'
print(Bank_greeting)

# supplied_pin = input("Please enter your PIN")
# Set PIN and tries in these variables
my_pin = '2205'
max_tries = 3

# Defined that PIN is verified if equal to variable set
def verify_pin(the_pin):
    return the_pin == my_pin

#
# Defined main function to set parameters
def main():
    tries = 0

    # Set a while loop to break if correct
    # Otherwise loop 3 times then end with locked account

    while tries < max_tries:
      pin = input("Please enter your PIN")
      if verify_pin(pin):
            print("PIN Correct: Welcome Serene")
            break
      else:
            print("Incorrect PIN. Please try again:")
      tries += 1
    else:
        print("Account Locked: Please contact 'Bank of Mum' for further assistance:")

# Driver code
if __name__ == '__main__':
    main()
