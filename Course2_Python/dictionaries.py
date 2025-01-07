sample_dict = {1:"test", "Name": "Val", 3:"juice", 1: "Not a test"}
# Se eu colocar chaves repetidas, ele vai sobrescrever com o valor da última chave

# Change one item
#sample_dict[2]="Mint tea"

# Delete
# del sample_dict[3]
# change the value
#sample_dict[1] = "Not a test"

for x in sample_dict:
    print(x)

# Como iterar o dictionary
# Standart: items() or values()
for key,value in sample_dict.items():
    print(str(key) + " : " + value)