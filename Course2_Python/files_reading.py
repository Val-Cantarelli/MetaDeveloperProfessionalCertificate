# read(): reads the entire content of the file as a string. 
# You can take a part of it, for exemplo: 
# file.read(40) - it will read 40 characters

# readlines(): reads the entire content of the file and returns 
# it in an ordered list 

# readline(): return a single line as a string -the first line ou you can 
# read 30 charates like read()

with open("./Course2/newFile.txt",'r') as file:
    print(file.readlines())
    
# You can calculate all the lines of the file:
#lines = file.readline()
#print(len(lines))    


