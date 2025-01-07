import pandas as pd

a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

print(a)
print(a.describe())# function in pandas that will give the count, frequency, top values and frequency among other values.

b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

print(b.sort_values(by="Numbers"))# sorting function that will provide a sorted table leading to shuffling of the data entries in the table.

b = b.assign(new_values = b['Numbers']* 3)# unction takes the values present inside the table, performs an operation over them and creates a new variable called new_values that is then added to the table.
print(b)