#What will be the length of following set S:
s = set()
s.add(20)   #This line adds the integer 20 to the set 's'.  
s.add(20.0) #This line adds the float 20.0 to the set 's'. However, since 20 and 20.0 are considered equal in Python, it will not be added as a separate element.
s.add("20") #This line adds the string "20" to the set 's'. This is a different element from the integer 20 and the float 20.0, so it will be added to the set.
print(len(s)) #This line prints the length of the set 's', which will be 2, because the set contains the integer 20 (which is considered the same as 20.0) and the string "20".