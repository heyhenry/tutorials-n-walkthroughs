# Ask user for their name
name = input("What's your name? ")

# Say hello to user
# The usage of the innate parameter 'end=' to cancel out its default newline execution and 
# instead provide no space so that the next print statement is displayed on the same line, 
# portraying a sense of continuity or concatenation.
print("Hello, ", end="")
print(name)