numbersFile = open("numbers.txt", "r+")
total = [0]
i = 0
while numbersFile.readline() != "":
    total += numbersFile.readline().split("\n")

print(total)
numbersFile.close()