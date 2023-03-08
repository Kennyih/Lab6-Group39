#Isabelle Kenny
#Brian D. Miller II

#Encoder
def encode(password):
    #Change the string to an array
    arr = [int(x) for x in str(password)]
           
    #Checking if password has exactly 8 digits
    # - Brian
    if len(password) != 8:
        print("Error: Password must have exactly 8 digits")
           
    else:

       #Has to be 8 characters
        i = len(arr)
        for i in range(i,8):
            arr.append(0)
        #'Encoding' the password so that each number is +3
        for j in range(8):
            #If the encoded number is greater than 9, it will loop back to 0. - Brian
            #i.e. input = 7, output = 0; input = 8, output = 1; input = 9, output = 2, etc
            temp = (arr[j] + 3) % 10
            arr[j] = temp

        #Converting back to string to print
        new = ''.join(map(str, arr))

        print("Your password has been encoded and stored!\n ")
        return new

#Decoder - Brian
def decode(encodedPass):

    #Setting up an exception for blank passwords. - Brian
    try:
        if not encodedPass:
            raise ValueError("Error, No password inputted")
        
        #Basically just doing the same thing, but in reverse. - Brian
        #Change the string to an array
        arr = [int(x) for x in str(encodedPass)]

       #Has to be 8 characters
        i = len(arr)
        for i in range(i,8):
            arr.append(0)
        #'Decoding' the password by subtracting 3 from each value.
        for j in range(8):
            temp = arr[j] - 3
            if temp <0:
                temp = 10 + temp
            arr[j] = temp

        #Converting back to string to print
        originalPass = ''.join(map(str, arr))
        
        print(f"The encoded pasword is {encodedPass}, and the original password is {originalPass}.")

    except (ValueError):
        print("Error: No password inputted")

#main
menu = True
#Instantiate encodedPass so the program doesn't crash if you try to decode without inputting anything.
encodedPass = ""

#while true, run menu
while menu:
    #menu options
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    userInput = int(input("\nPlease enter an option: "))
    #If 3 : Exit
    if userInput == 3:
        menu = False
        pass
    #if 1: Encode a password
    if userInput == 1:
        password = input("Please enter your password to encode: ")
        encodedPass = encode(password)

    #if 2: Decode the password
    if userInput == 2:
        decode(encodedPass)
