userName = input("What is your name?:\t")
nameFile = open("name.txt", "w")
nameFile.write(userName)
nameFile.close()
