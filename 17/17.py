import datetime
start = datetime.datetime.now()
data = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]; volume = 150

combinations = []
for i in range(0, 2**(len(data))):
    result = []
    binary = bin(i)[2:]
    binary = "0"*(len(data) - len(binary)) + binary
    for index, char in enumerate(binary):
        if char == "1":
            result.append(data[index])
    if sum(result) == volume:
        combinations.append(result)

print("Task 1:",len(combinations))
length = []
for combination in combinations:
    length.append(len(combination))

print("Task 2:",length.count(min(length)))
print("Runtime: ", datetime.datetime.now() - start)