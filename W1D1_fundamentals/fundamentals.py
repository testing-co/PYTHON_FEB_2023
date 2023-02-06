# ===================
# PYTHON FUNDAMENTALS
# ===================
"""
this is a multiline comment!
see?!!!!
"""
# variables
snake_case = "all lower case, separated by underscore"
GLOBAL_VAR = "ALL CAPS"

# PRIMITIVE VARIABLES:
# boolean
vote = True
is_admin = False

my_num = 6
float_num = 3.14

name = "john"
my_string = "a collection of characters!"
formatted_string = f"we can inject variables! {my_num}"

concat_string = "my number is " + str(my_num)
print(concat_string)

# ---------------------
# composite types (Classes under the hood)
# list - aka arrays in JS!
#          0 1 2 3 4
my_list = [1,2,3,4,5] # they are 0 indexed/mutable
my_list[1] # 2
my_list.append(1337) # .push(123)

print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort(reverse=True)
print(my_list)

print(f"the length of this list is =   {len(my_list)}"  )

# dictionaries aka objects in JS
# don't have an index
# key-value pairs
# comma separated

dog_dict = {
    'name' : "Mochi",
    'age' : 3,
    'breed' : "corgi",
    'is_a_good_boi': True,
    # 'name': "Rex"
}
print(dog_dict)
dog_dict['name'] = "Booboo"
# print(dog_dict['size']) # can't do this

int_to_complex = complex(35)
print(int_to_complex)

# --- tuples ---------
# cannot be changed - immutable

#      0  1  2     3
tup = (11,22,33, "bob")
# tup[0]

# tup[0] = 1000

# --------conditionals--------
# if
# elif
# else

x = 8

if x == 5:
    print("x is 5")
    b = x
    print("hi")
elif x > 5:
    print("x is big!")
else:
    print("x is smol")
    
"""
Py        |      JS
====================
None            null
not              !
or               ||
and              &&
is <-- used to check if both operands are the same object in memory

"""

