import array as arr

array_num= arr.array("i", [1,2,3,4,5,6,7,3,3,3,3])
print("Original array is:", array_num)

print("Number of occurences of the number 3 is:", array_num.count(3))

array_num.reverse()
print("Reversed array is:", array_num)
