def read_file(file_name):
    # function to read in the sampletext.txt file using 
    # the `open` function and return the entire contents of the file
    with open(file_name, "r") as file:
        data = file.read()
        print(data)
    return data

def read_file_into_list(file_name):
    # Reads in a file and stores each line as an element in a list  
    with open(file_name, "r") as file:
        data = file.readlines()
    return data

#def write_first_line_to_file(file_contents, output_filename):
# Writes the first line of a string to a file. 
# 1. Get the first line of file_contents        
# 2. Use the File write() function to write the first line into a file with the name from output_filename 
# We determine the first line to be everything in a string before the
# first newline ('\n') character.    Args:        file_contents: string to be split and written 
# into output file        
# output_filename: the name of the file to be written to    """    
    with open(output_filename, "w") as file:
        file.write(file_contents.split("\n")[0])
    return file
        

#def read_even_numbered_lines(file_name):
    
    with open(file_name, "r") as file:
        even_lines = []
        lines = file.readlines()     
        for i in range(1,len(lines),2):
            even_lines.append(lines[i])
    return even_lines

#def read_file_in_reverse(file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
        data.reverse()
        
    return data    

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("./Course2/sampletext.txt")
    print(read_file_into_list("./Course2/sampletext.txt"))
    #print(write_first_line_to_file(file_contents, "online.txt"))
    #print(read_even_numbered_lines("./Course2/sampletext.txt"))
    #print(read_file_in_reverse("./Course2/sampletext.txt"))

if __name__ == "__main__":
    main()