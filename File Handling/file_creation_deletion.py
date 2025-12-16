import os

# Create a new file
f = open("myfile.txt","x")
f.write("Hello World")
f.close()

# Delete file
os.remove("myfile.txt")

# Create folder if not exists
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
else:
    print("Folder already exists.")
