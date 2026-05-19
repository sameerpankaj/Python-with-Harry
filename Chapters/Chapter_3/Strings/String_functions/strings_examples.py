'''
Common String Operations
1. Change Case
text.lower()        # hello world
text.upper()        # HELLO WORLD
text.title()        # Hello World
text.capitalize()   # Hello world
text.swapcase()     # hELLO wORLD
2. Remove Spaces / Characters
text.strip()        # Removes spaces from both ends
text.lstrip()       # Left side
text.rstrip()       # Right side
3. Search / Find
text.find("World")      # Returns index
text.index("World")     # Similar but gives error if not found
text.count("o")         # Count occurrences
4. Replace Text
text.replace("World", "Python")
5. Split and Join
text.split()            # ['Hello', 'World']
",".join(["A", "B"])    # A,B
6. Check Content
text.startswith("Hello")
text.endswith("World")
text.isalpha()
text.isdigit()
text.isalnum()
text.isspace()
7. Formatting Strings
name = "Sameer"
f"Hello {name}"         # f-string
"Hello {}".format(name)
8. Access Characters
text[0]     # H
text[-1]    # d
text[0:5]   # Hello
9. Length
len(text)
10. Reverse String
text[::-1]
Escape Characters
\n   # New line
\t   # Tab
\\   # Backslash
\'   # Single quote
\"   # Double quote
Useful Examples
"python".center(10)
"42".zfill(5)
"hello".encode()
Most Important Ones for Daily Use
lower()
upper()
strip()
replace()
split()
join()
find()
startswith()
endswith()
format()
f-strings
Pro Tip:

For modern Python, f-strings are the preferred way:

age = 39
print(f"I am {age} years old")

'''