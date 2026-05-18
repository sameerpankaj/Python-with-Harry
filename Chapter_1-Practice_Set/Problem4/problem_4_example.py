import os

# --- 1. List contents of the current directory ---
print("=== Current Directory Contents ===")
current_dir = os.getcwd()  # Get the current working directory
print(f"Path: {current_dir}\n")

contents = os.listdir(current_dir)
for item in contents:
    print(item)

# --- 2. Distinguish files from subdirectories ---
print("\n=== Files vs Directories ===")
for item in contents:
    full_path = os.path.join(current_dir, item)
    if os.path.isfile(full_path):
        print(f"[FILE] {item}")
    elif os.path.isdir(full_path):
        print(f"[DIR]  {item}")

# --- 3. List contents of a specific directory ---
print("\n=== Specific Directory (e.g., /tmp) ===")
specific_path = "C:\Python"  # Change this to any path you like
try:
    for item in os.listdir(specific_path):
        print(item)
except FileNotFoundError:
    print(f"Error: '{specific_path}' does not exist.")
except PermissionError:
    print(f"Error: No permission to access '{specific_path}'.")



#     Key points from the docs:

# os.listdir() returns a list of all entry names in the given directory, in arbitrary order, and does not include the special entries . and ... Python
# If no path is provided, it defaults to the current directory ('.'). GeeksforGeeks
# It can raise FileNotFoundError if the path doesn't exist, NotADirectoryError if the path isn't a directory, and PermissionError if access is denied GeeksforGeeks — so wrapping it in a try/except block is good practice.