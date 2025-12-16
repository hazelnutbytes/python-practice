# Open and read
with open("demofile.txt") as f:
    print(f.read())

# Read line by line
f = open("demofile.txt")
print(f.readline())
f.close()
