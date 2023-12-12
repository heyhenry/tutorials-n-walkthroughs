# Ask user for their name
# ----
# name = input("What's your name? ")

# Say hello to user
# The usage of the innate parameter 'end=' (also known as named parameters) to cancel out its default newline execution and 
# instead provide no space so that the next print statement is displayed on the same line, 
# portraying a sense of continuity or concatenation.
# ----
# print("hello ", end="")
# print(name)
# print("---")
# print("hello,", name, sep="!!!", end="")
# print(name)

# Alternative way to include dynamic variable name is by using string.format as below:
# print(f"Hello, {name}")

# String manipulations - Quotations
# For sentences that use multiple quotations, you can utilise either the following: 
# This ensures different quotations are used
# ----
# print("Hello, 'friend'")

#Alternatively, you can use the back-slash to indicate to the computer that said quotes are quotations that finish or start a sentence, 
# rather they are literal quotes used for selected word/s
# ----
# print("Hello, \"friend\"")

# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize user's name (only capitalize's first character)
# name = name.capitalize()

# Capitalize first character of each word
# name = name.title()  

# Say hello to user
print(f"hello, {name}")