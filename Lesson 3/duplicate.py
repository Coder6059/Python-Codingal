student_data = {
    "id1": {
        "name": "John",
        "class": "8th",
        "subject": "Math"
    },
        "id2": {
        "name": "Alex",
        "class": "8th",
        "subject": "Math"
},
    "id3": {
        "name": "John",
        "class": "8th",
        "subject": "Math"
},
    "id4": {
        "name": "Alice",
        "class": "8th",
        "subject": "Math"
}
}

result = {}
seen_keys = []

for id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"]) 
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[id] = details
for x,y in result.items():
    print(x,":",y) 