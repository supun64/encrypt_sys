# This is a small encrypted system for messages
# This is the code to encrypt a message with 25 characters


def encrypt(alpha_msg):

    grid = list(map(lambda x: ["-"]*5, list(range(5))))

    # These are the variables for a looping type
    ai = 4  # constant
    aj = 4
    aj_e = 0

    # These are the variables for b looping type
    bi = 3
    bi_e = 0
    bj = 0

    # These are the variables for c looping type
    ci = 0  # constant
    cj = 1
    cj_e = 4

    # These are the variables for d looping type
    di = 1
    di_e = 3
    dj = 4  # constant

    num = -1  # This is the index of message to assign to grid

    while num >= -25:

        # a loop
        for a in range(aj, aj_e - 1, -1):
            grid[ai][a] = alpha_msg[num]
            num -= 1

        ai -= 1
        aj -= 1
        aj_e += 1

        # b loop
        for b in range(bi, bi_e - 1, -1):
            grid[b][bj] = alpha_msg[num]
            num -= 1

        bi -= 1
        bi_e += 1
        bj += 1

        # c loop
        for c in range(cj, cj_e + 1):
            grid[ci][c] = alpha_msg[num]
            num -= 1

        ci += 1
        cj += 1
        cj_e -= 1

        # d loop
        for d in range(di, di_e + 1):
            grid[d][dj] = alpha_msg[num]
            num -= 1

        di += 1
        di_e -= 1
        dj -= 1

    # grid[2][2] = alpha_msg[num] # This is the code to assign the last value of message to the middle of the grid

    # Creating the list of characters in grid in row by row
    char_list = list(char for row in grid for char in row) 

    return "".join(char_list)


# This is the function to decrypt a encoded message   
def decrypt(encode):

    # This is the grid which has the encoded message
    grid = list(list(encode[i: i + 5]) for i in range(0, len(encode), 5))
    alpha_msg = ""
    
    # These are the variables for a looping type
    ai = 4  # constant
    aj = 4
    aj_e = 0

    # These are the variables for b looping type
    bi = 3
    bi_e = 0
    bj = 0  # constant

    # These are the variables for c looping type
    ci = 0  # constant
    cj = 1
    cj_e = 4

    # These are the variables for d looping type
    di = 1
    di_e = 3
    dj = 4  # constant

    num = -1

    while num >= -25:

        # a loop
        for a in range(aj, aj_e - 1, -1):
            alpha_msg += grid[ai][a]
            num -= 1

        ai -= 1
        aj -= 1
        aj_e += 1

        # b loop
        for b in range(bi, bi_e - 1, -1):
            alpha_msg += grid[b][bj]
            num -= 1

        bi -= 1
        bi_e += 1
        bj += 1

        # c loop
        for c in range(cj, cj_e + 1):
            alpha_msg += grid[ci][c]
            num -= 1

        ci += 1
        cj += 1
        cj_e -= 1

        # d loop
        for d in range(di, di_e + 1):
            alpha_msg += grid[d][dj]
            num -= 1

        di += 1
        di_e -= 1
        dj -= 1

    return alpha_msg[::-1]


# #This is the  function of the program
def program():
    # See if user has to do a encrypting or decrypting
    command = input("Do you want to encrypt a message or decrypt a message (E/D): ").upper()
    alphabet = list(chr(i) for i in range(ord("a"), ord("z") + 1))
    
    # #Code if user has to encrypt
    if command == "E":
        message = "".join(input("Enter the message: ").lower().split(" "))

        # Encrypt a message which has no more than 25 characters
        if len(message) < 25:
            message += "".join(alphabet[:25 - len(message)])
            print(encrypt(message))  # last output

        # Encrypt a message which has more than 25 characters
        else:
            # if 25 is not a factor of character number of message
            if len(message) % 25 != 0:
                message += "".join(alphabet[:25 - len(message) % 25])

            # dividing the message into 25 slices
            message_divides = list(message[i:i+25] for i in range(0, len(message), 25))
            encrypted_message = ""

            for part in message_divides:
                encrypted_message += encrypt(part)  # encrypt one by one 25 charcter parts and curcatenade them

            print(encrypted_message)  # Last output

    # #This is the code want to decrypt a encoded message
    elif command == "D":
        text = input("Enter encrypted message: ")
        if len(text) % 25 != 0:
            text += "".join(alphabet[:25 - len(text) % 25])
        text_slices = list(text[i:i + 25] for i in range(0, len(text), 25))
        decrypt_message = ""

        for part in text_slices:
            decrypt_message += decrypt(part)

        print(decrypt_message)

    elif command == "":
        print("Thank you for using Encrypt 1.0.".center(100, "!"))
        print("*"*100)
        return True


# Execution of functions
print("Enter 'D' for Decrypt and 'E' for Encrypt,\n"
      "press enter without any text for exit the program")
print("-"*100, "\n")

while True:
    program_running = program()
    if program_running:
        break
    print("-"*100, "\n")
