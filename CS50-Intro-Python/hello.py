# Ask user for their name
name = input("What's your name? ")

# Say hello to user
# The usage of the innate parameter 'end=' (also known as named parameters) to cancel out its default newline execution and 
# instead provide no space so that the next print statement is displayed on the same line, 
# portraying a sense of continuity or concatenation.
print("hello ", end="")
print(name)
print("---")
print("hello,", name, sep="!!!", end="")
print(name)