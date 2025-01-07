"A map takes all objects in a list and applies a function"
"A filter do the same, but takes the results and creates a new list with only the true values"

menu = ["espresso", "mocha", "capuccino", "cortado"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

# map_coffee = map(find_coffee,menu)

# for i in map_coffee:
#     print(i)

filter_coffee = filter(find_coffee,menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
    
    
# Neste exemplo se trocarmos filter por map vai retornar todos os elementos(é como o map funciona), 
# mas com o resultado da função aplicada em cada um(true/false)  

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)

#Output com filter:[15,30,47]
    
#Output com map: [True, True, True, False, False]   