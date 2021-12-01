#AoC 2015 - Day 4
# https://www.geeksforgeeks.org/md5-hash-python/

import hashlib, datetime
start = datetime.datetime.now()

def md5finder(input, leadingZeros):
    counter = 0
    while True:
        textToEncode = input + str(counter)
        result = hashlib.md5(textToEncode.encode())
        if result.hexdigest()[0:leadingZeros] == "0" * leadingZeros:
            break
        counter += 1
    return counter

#MAIN:
input = "yzbqklnj"

print("Task 1: Code with 5 zeros: {0}".format(md5finder(input, 5)))
print("Runtime: {0}".format(datetime.datetime.now()-start))
print("Task 2: Code with 6 zeros: {0}".format(md5finder(input, 6)))
print("Runtime: {0}".format(datetime.datetime.now()-start))