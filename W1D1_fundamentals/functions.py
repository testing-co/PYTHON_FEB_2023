# what is a function?
# set a of instructions
# repeatable code?
# take in parameters
# will ALWAYS return something

# print(print("hi"))
def greeting():
    print("hello ninja!")
    # return "hello ninja"
    
def say_hello(name="ben", times=10):
    for i in range(times):
        x = f"hello {name}"
        print(f"{i+1} hello {x} --- times //// {times/2}")
    
    
    
# say_hello(times=6, name="bob")

# call / invoke / run
# print(greeting())
# result = greeting()
# print(result)

#! A FUNCTION CALL IS EQUAL TO ITS RETURN


# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    new_list =[]
    for x in range(num, 0-1, -1) :
        print(x)
        new_list.append(x)
    return new_list

print(
    
countdown(5)
)
