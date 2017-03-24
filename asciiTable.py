""" ChrInput = prompt Enter character:
    print ("The ASCII code for {} is {}".format(ChrInput, ord(ChrInput))


    Numinput = prompt Enter number between 33 and 127
        if NumInput < 33 or NumInput > 127
            print("Error: Invalid Number")
        else
            print ("The ASCII code for {} is {}".format(NumInput, chr(NumInput))


"""
upper = 127
lower = 33
chrInput = input("Enter character:")
print ("The ASCII code for {} is {}".format(chrInput, ord(chrInput)))
numInput = int(input("Enter Number between {} and {}:".format(lower, upper)))
if numInput < lower or numInput > upper:
    print("Error: Invalid Number")
else:
    print ("The character for {} is {}".format(numInput, chr(numInput)))

number = 32
while number is not 127:
    number += 1
    print("{:3} \t {:}".format(number, chr(number)))

