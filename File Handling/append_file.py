# Append content to existing file
with open("data.txt","a") as f:
    f.write("\nNow the file has more content!")

# Read after append
with open("data.txt") as f:
    print(f.read())
