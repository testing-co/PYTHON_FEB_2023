#  LOOPS

# for loops

# for __iterator___ in __collection range()____ :

# range() - is a function that return a sequence of numbers
# range() 

# 1-10
end = 10
for i in range(end+1):
    pass
    # print(i)

# 2-10 ,2
for num in range(2, 10+1, 2):
    pass
    # print(num)

#  10 -> 5
for x in range(10, 5-1, -1):
    pass
    # print(x)
    
for element in range(10):
    pass
    # print(element)

# ? iterate over a list
#            0            1         2         3         4
food_list = ['pizza', 'cheese', 'ramen', 'sushi', 'more cheese']  # 5
# food_list[0]
# food_list[1]
# print(len(food_list))

# for i in range(len(food_list)) :
#     print(food_list[i])

for item in food_list:
    pass
    # print(item)
    
#? ------------ DICTIONARIES ---------

cat1 = {
    'name' : 'Cinnamon',
    'age' : 7,
    'color' : 'orange'
}
# print(cat1['name'])

cat2 = {
    'name' : 'Bunny',
    'age' : 2,
    'color' : 'black'
}

cat_list = [cat1, cat2]

for element in cat_list:
    print(element)
    for cat_key in element:
        print(element[cat_key])
    
# print(cat_list)

# for key_dict in cat1:
#     print(key_dict, cat1[key_dict])
    
capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
}

for some_key in capitals:
    print(f"the capital of {some_key} is {capitals[some_key]}")

# just get the values
# for val in capitals.values():
#     print(val)

# for state_key, state_capital in capitals.items():
#     print(state_key, state_capital)