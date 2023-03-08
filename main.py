def encode(password):
    arr = [int(x) for x in str(password)]
    i = len(arr)
    for i in range(i,8):
        arr.append(0)
    for j in range(8):
        temp = arr[j] + 3
        arr[j] = temp

    new = ''.join(map(str, arr))

    print("Your password has been encoded and stored!\n ")
    return new


menu = True
while menu:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    userInput = int(input("\nPlease enter an option: "))

    if userInput == 3:
        menu = False
        pass
    if userInput == 1:
        password = input("Please enter your password to encode: ")

        encodedPass = encode(password)
    if userInput == 2:
        decode(encodedPass)
