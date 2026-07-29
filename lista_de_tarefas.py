import json
#Declarar
tarefas:str = []
acao: int = 0
c: int = 0
nova_tarefa: str = ""
#Módulos
def carregar (tarefas):   
    try:
        with open("ListaTarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
        print ("Lista já existente")
        arquivo = int(input("Deseja: 1 Deletar e criar nova ou 2 Manter lista?"))   
        if (arquivo==1):
            tarefas = []
            return tarefas
        elif(arquivo==2):
            return tarefas
    except:            
        with open ("ListaTarefas.json","w") as arquivo:
            json.dump(tarefas, arquivo)
            return tarefas

def salvar(tarefas):
    with open ("ListaTarefas.json","w") as arquivo:
        json.dump(tarefas, arquivo)

def criar(tarefas):
    while (True):
        nova_tarefa = str(input("Adicione uma tarefa (ou 'sair' para voltar): "))
        if (nova_tarefa == "sair"):
            break
        else:
            tarefas.append(nova_tarefa)
        
def listar(tarefas):
    print ("\n")
    if (len(tarefas)==0):
        print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa)

def concluida(tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa)

        while (True):
            try:
                c = int(input ( "\nDigite o número da tarefa que está concluída (ou '0' para voltar):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    if not tarefas[c].endswith(" - Concluída"):
                        tarefas[c] = tarefas[c] + " - Concluída"
                    else:
                        print("Essa tarefa já está concluída")
            except:
                print("Número inválido. Digite um número da lista.")
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa)

def remover (tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa)
        while (True):
            try:
                c = int(input("\nDigite o número da tarefa que será deletada(ou '0' para sair):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    print("Tarefa deletada: " + tarefas.pop(c))
            except:
                print("Número inválido. Digite um número da lista.") 

def editar (tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa)
        while (True):
            try:
                c = int(input("\nDigite o número da tarefa que será editada(ou '0' para sair):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    tarefa_concluida = tarefas[c].endswith(" - Concluída")
                    if (tarefa_concluida):
                        tarefas[c] = tarefas[c].removesuffix(" - Concluída")
                    else: 
                        tarefas[c] = tarefas[c]
                    print("Tarefa atual:",tarefas[c])
                    tarefas[c] = input("Digite o novo texto: ")
                    if (tarefa_concluida):
                        tarefas[c] = tarefas[c] + " - Concluída"
                    else:
                        tarefas[c] = tarefas[c]
            except:
                print("Número inválido. Digite um número da lista.") 

#Inicio
tarefas = carregar (tarefas)
while (acao!=6):
    print ("\n1 Adicionar uma tarefa \n2 Listar todas as tarefas \n3 Marcar uma tarefa como concluída \n4 Remover uma tarefa \n5 Editar tarefa\n6 Sair do programa")
    try:
        acao = int(input("Escolha uma das ações acima:")) 
    except:
        print("Número inválido. Digite um número da lista.")
    if (acao==1):
        criar(tarefas)
        salvar (tarefas)
    elif (acao==2):
        listar(tarefas)
    elif (acao==3):
        concluida(tarefas)
        salvar (tarefas)
    elif (acao==4):
        remover(tarefas)
        salvar (tarefas)
    elif (acao==5):
        editar(tarefas)
        salvar (tarefas)
    elif (acao==6):
        print ("Saindo do Programa")
    else:
        print ("ERRO")
        print ("A ação digitada não existe, por favor digite um número válido")
#Fim

