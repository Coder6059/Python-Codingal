gradebook = {"Sam" : 95, "Dave" : 68, "Kunal" : 90, "Peter" : 100, "Daniel": 79}

avg = 0
for i in gradebook:
    avg+=gradebook[i]
avg = avg / 5
print(avg)


input_name = input("Enter a name:")
find_name = gradebook.get(input_name, "Sorry, name not found")
print(find_name)

max_score = max(gradebook.values())
print(max_score)

min_score = min(gradebook.values())
print(min_score)