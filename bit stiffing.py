
data = input("Enter the data bits(0/1): ")
stuffed=" 110"
count= 0
for bit in data:
    if bit=="1":
        count+=1
    else:
        count=0
    stuffed+=bit
    if count==5:
        stuffed+="0"
        count=0
print("After bit stuffing:",stuffed)
