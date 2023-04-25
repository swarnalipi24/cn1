
message = input("Enter the message :")
stuffed = " "
for i in range(len(message)):
    if message[i:i+3]=="DLE":
        stuffed+="DLEDLE"
    else:
        stuffed+=message[i]
print("After character stuffing: ", stuffed)