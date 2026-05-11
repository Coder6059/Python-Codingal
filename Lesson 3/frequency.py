dict = {"codingal" : 2, "is": 3, "the": 4, "best":3, "for": 5, "coding": 1}
print("the original dictionary", dict)

v = 3
count = 0

for key in dict:
    if dict[key] == v:
        count = count + 1

print("the frequency of 3 is ", count)