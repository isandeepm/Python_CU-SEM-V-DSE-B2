
import os

print("OUTPUT-1")

# Open a file
f = open('myfile1.txt', 'r') # 'r' for reading

# Read the contents of the file
contents = f.read()
print(contents)

# Check the current position in the file (at the beginning)
print(f.tell()) # returns 0

# Move the position in the file

print(f.seek(5)) # move the position to the 6th byte in the file

# Read from the current position
print(f.read())

# Write to the file
f = open('myfile1.txt', 'w') # 'w' for writing (overwrites file)
f.write('Hello, world!')

# Append to the file
f = open('myfile1.txt', 'a') # 'a' for appending
f.write('\nThis is a new line')
f = open('myfile1.txt', 'r')
print(f.read())

# Close the file
f.close()


print("OUTPUT-2")

# Open a file
f = open('myfile2.txt', 'r') # 'r' for reading

# Read the contents of the file
contents = f.read()
print(contents)

# Check the current position in the file (at the beginning)
print(f.tell()) # returns 0

# Move the position in the file
print(f.seek(10)) # move the position to the 6th byte in the file

# Read from the current position
print(f.read())

# Write to the file
f = open('myfile2.txt', 'w') # 'w' for writing (overwrites file)
f.write('Hi there!')

# Append to the file
f = open('myfile2.txt', 'a') # 'a' for appending
f.write('\nNew line added')
f = open('myfile2.txt', 'r')
print(f.read())

# Close the file
f.close()
