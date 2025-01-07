#Compreensões são uma forma de criar uma nova sequência a partir de uma sequência já existente. Map são mais eficientes quando
# falamos de uma grande quantidade de dados

# List comprehension 

"The syntax for list comprehension is:[ <expression> for x in <sequence> if <condition>] "

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)



# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

# EX6:Para cada elemento i na lista z, 
#ele pega a primeira letra do elemento e multiplica n vezes
z = ["alpha","bravo","charlie"]
new_z = [i[0]*3 for i in z]
print(new_z)


"Exemplo da diferença entre alterar a lista normalmente por loop ou por compressão"

# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

#____________________________________________________________________
# Dictionary comprehension 
"The syntax for dictionary comprehension is:dict = { key:value for key, value in <sequence> if <condition> } "
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)
#_________________________________________________________________________________
# Set comprehension 

set_a = {x for x in range(10,20) if x not in [12,14,16]} 
# Para mostrar versatilidade, usei as palavras-chave “not in” para verificar os valores da lista. 
# A saída são os valores nos intervalos 10 e 20 que não estão presentes nessa lista.
print(set_a)



# Generator comprehension
# As compreensões do gerador também são muito semelhantes às listas, com a variação de usar parenteses em vez de colchetes. 
# Eles também são mais eficientes em termos de memória em comparação com a compreensão de listas. Por exemplo:
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")
# Ps: a list foi modificada em todos os passos

