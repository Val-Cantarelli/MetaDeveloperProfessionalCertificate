#Example of NOT pure function
# 
# 
# my_list = [1,2,3]

#def addList(item):
#return my_list.append(item)

#addList(4)

#print(my_list)


" Para que fosse pura, precisei primeiro copiar(ter 2 endereços de memória diferentes) a lista que "
" passei em outra variável.O append modifica a lista."
myList = [1,2,3]

def addList(list,item):
    newList = list.copy()
    newList.append(item)
    newList.reverse()
    return newList

print(addList(myList,4))
print(myList)



