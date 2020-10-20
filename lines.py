file = open("e:\\Newfile.txt")
file.read()
arr = []  
line = 1
for word in read: 
    if word == '\n': 
        line += 1
print("Number of lines in file is: ", line) 

for i in range(line): 
    arr.append(file.readline())
    
