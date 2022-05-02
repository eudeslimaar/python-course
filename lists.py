demo_list= [1, "hello", 1.34, True, [1,2,3,4]]
colors = ["red","green","blue"]

# mutable list

mutable_list = [1,2,3,'blue',5]
print(type(mutable_list))
print(mutable_list)
print(len(mutable_list))
print(mutable_list.index('blue')) # index of blue is 3.
mutable_list[3] = 'red'
print(mutable_list)

# immutable list

inmutable_list = (1,2,3,'green', 5)
print(type(inmutable_list))
print(inmutable_list)
print(len(inmutable_list))
print(inmutable_list.index(3)) # index of 2.
# inmutable_list[2] = 'white' # will not be possible and will warn with an error.
print(inmutable_list)

listRange = []

# to create a list range
listRange = list(range(1,100))

print(len(listRange))
listRangevalue = 40
print(f"{listRangevalue} is {listRangevalue in listRange}!")

# to append a new value, but only one value.

listRange.append(101)
listRangevalue = 101
print(f"{listRangevalue} is {listRangevalue in listRange}!")
print(len(listRange))
print(listRange.index(101))
print(listRange[99])

# To extend the list with more values, use "extend"
new_list = []
print(new_list)
new_list = list(range(1,10))
print(new_list)
new_list.extend([10,11,12,13,14,15])
new_listValue = 14
print(f'the value {new_listValue} is { new_listValue in new_list}!')
print(f'"new_list" have new {len(new_list)} elements!')
print(new_list.index(15))
new_list.insert(15, 16)
print(new_list)
new_list.insert(len(new_list), 17)
print(f'"new_list" have new {len(new_list)} elements!')


colors.extend(["white","pink","lightblue","salmon","orange"])
#colors.pop() remove methods
#colors.remove('white') remove methods
#colors.pop(0) remove methods
print(colors)

colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)


