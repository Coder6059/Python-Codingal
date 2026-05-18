dict = {'Codingal': 2, 'is':3, 'the': 3, 'best':3, 'for':3, 'coding':1}

v = 3
count = 0

for key in dict:
    if dict[key] == v:
        count = count + 1

print("the frequency of 3 is ", count)