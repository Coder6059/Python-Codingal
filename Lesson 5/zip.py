s1 = {2,3,1}
s2 = {"b", "c", "a"}
s3 = list(zip(s1,s2))
print(s3)

list1 = [10,20,30,40,50]
list2 = [100,200,300,400,500]

for x,y in zip(list1, list2[::-1]):
    print(x,y)

stocks = ["reliance", "infosys", "tcs"]
prices = [2134, 36763, 38678]

new_dict = {stocks : prices for stocks, prices in zip(stocks, prices)}
print(new_dict)