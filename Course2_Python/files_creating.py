try:
    with open("./Course2/sampleFile.txt","a") as file:
        file.writelines(["\nteste1", "\nteste2"])
except FileNotFoundError as e:
    print("Error", e)
    
# I try make this an Error, but the function created a file    