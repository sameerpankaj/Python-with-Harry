#Write a program to greet all the person names stored in a list 'l' and which starts with S
# List of names
_names = ["Harry", "Soham", "Sachin", "Rahul",]
# Loop through the list of names
for name in _names:
    # Check if the name starts with 'S'
    if name.startswith("S"):
        print(f"Hello, {name}!")  # Greet the person whose name starts with 'S'