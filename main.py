import os
import shutil

Caminho = []

letra_do_disco = 'C'
pasta1 = 'Users'
pasta2= 'public'

Caminho.append(letra_do_disco)
Caminho.append(pasta1)

#procura o diretorio de usuario
k = os.listdir((Caminho[0] +':/' + Caminho[1]))

for v in k:
    if ((v != 'Public') and (v != 'All Users') and (v != 'Default') and (v != 'Default User') and (v != 'desktop.ini') and (v != 'Downloads') and (v != 'Todos os Usuários') and (v != 'Usuário Padrão') ):
        Caminho.append(v)
        print(Caminho)

#entra no diretorio documentos
i = os.listdir((Caminho[0] +':/' + Caminho[1]+ '/' + Caminho[2]))

for j in i:
    if j =='Documents':
        Caminho.append(j)
        print(Caminho)


Documentos = os.listdir((Caminho[0] +':/' + Caminho[1]+ '/' + Caminho[2] + '/' + Caminho[3]))

for docs in Documentos:
    if docs != 'desktop.ini':
        Caminho.append(docs)
        print(Caminho)



