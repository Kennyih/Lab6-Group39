#Isabelle Kenny

#Encoder
def encode(password):
    #Change the string to an array
    arr = [int(x) for x in str(password)]

   #Has to be 8 characters
    i = len(arr)
    for i in range(i,8):
        arr.append(0)
    #'Encoding' the password so that each number is +3
    for j in range(8):
        temp = arr[j] + 3
        arr[j] = temp

    #Converting back to string to print
    new = ''.join(map(str, arr))

    print("Your password has been encoded and stored!\n ")
    return new

#Decoder - Partner

#main
menu = True

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
