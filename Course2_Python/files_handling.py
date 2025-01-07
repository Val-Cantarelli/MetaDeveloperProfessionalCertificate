# OPEN
#open (<file_name><file_location>, <mode>)
# <mode> it is the action: reading('r'), writing('w'), reading and writing('r+')or creating
# <mode> 'a' open to editing or appendind data
# output: text or binary

# In this way, you dont need close
#with open("testing.txt", r) as file:

# In Python, generally you will use file in text or binary.
# To open binary is the same process, but will need add the letter b: "rb", "rb+", "wb", "ab"

#CLOSE
#close() no args

#file = open("./Course2/test.txt", mode= "r")
with open("./Course2/test.txt", "r") as file:
    data = file.readline()
    print(data)




