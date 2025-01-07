'''Não importa quantas vezes você repita o import, o interpretador vai importar apenas uma vez. Pra isso temos 
a função reload() que recarrega o módulo quantas vezes vc quiser. Nesse caso, quando vc exclui ou cri um novo arquivo no diretorio
especificado e aperta "enter", ele dá reload com a lista de conteudo atualizado'''

import importlib
import filechanges
# Usa a reload() passando o filechanges como argumento
def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass
    
for i in range(5):
    changes()
   
    