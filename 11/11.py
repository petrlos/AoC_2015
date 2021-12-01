#AoC 2015 - Day 11

letters = "abcdefghijklmnopqrstuvwxyz"
doubles = [str(2*x) for x in letters]

def newPassword(password, where):
    if password[where] == "z":
        password = newPassword(password, where - 1)
    index = letters.index(password[where]) + 1
    if index == 26:
        index = 0
    if where == -1:
        password = password[0:where] + letters[index]
    else:
        password = password[0:where] + letters[index] + password[where + 1:]
    return password

def checkPassword(password):

    #NOT containts I, O, L
    for char in "iol":
        if char in password:
            return False

    #contains sequence abc, bcd, cde ...
    found = False
    for index in range(0,len(letters)-2):
        triplet = letters[index:index+3]
        if triplet in password:
            found = True
    if not found:
        return False

    #contains 2x same letter
    counter = 0
    for group in doubles:
        if group in password:
            counter += 1
    if counter < 2:
        return False

    return True

#MAIN

password = "cqjxjnds"

while True:
    if checkPassword(password):
        print(password)
        break
    password = newPassword(password, -1)

password = newPassword(password, -1)

while True:
    if checkPassword(password):
        print(password)
        break
    password = newPassword(password, -1)
