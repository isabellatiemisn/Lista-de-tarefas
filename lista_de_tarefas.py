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
        arquivo = int(input("Deseja: 1 Manter lista ou 2 Criar nova lista? "))   
        if (arquivo==1):
            return tarefas
        elif(arquivo==2):
            tarefas = []
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
        nova_tarefa = str(input("Adicione uma tarefa (ou 'sair' para voltar):"))
        if (nova_tarefa == "sair"):
            break
        else:
            tarefas.append({"tarefa":nova_tarefa,"concluida":False})
        
def listar(tarefas):
    print ("\n")
    if (len(tarefas)==0):
        print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            extra = " - Concluída" if tarefa["concluida"] else " "
            print(str(indice) + " - " + tarefa["tarefa"] + extra )

def concluida(tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa["tarefa"])

        while (True):
            try:
                c = int(input ( "\nDigite o número da tarefa que está concluída (ou '0' para voltar):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    if not (tarefas[c]["concluida"]):
                        tarefas[c]["concluida"] = True
                    else:
                        print("Essa tarefa já está concluída")
            except:
                print("Número inválido. Digite um número da lista.")
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa["tarefa"])

def remover (tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa["tarefa"])
        while (True):
            try:
                c = int(input("\nDigite o número da tarefa que será deletada(ou '0' para sair):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    removida = tarefas.pop(c)
                    print("Tarefa deletada: " + removida["tarefa"])    
            except:
                print("Número inválido. Digite um número da lista.") 

def editar (tarefas):
    if (len(tarefas)==0):
            print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            print(str(indice) + " - " + tarefa["tarefa"])
        while (True):
            try:
                c = int(input("\nDigite o número da tarefa que será editada(ou '0' para sair):"))
                if (c==0):
                    break
                else:
                    c = c - 1
                    print("Tarefa atual:",tarefas[c]["tarefa"])
                    tarefas[c]["tarefa"] = input("Digite o novo texto: ")
            except:
                print("Número inválido. Digite um número da lista.") 

#Inicio
tarefas = carregar (tarefas)
while (acao!=6):
    print ("\n1 Adicionar tarefa \n2 Listar tarefas \n3 Marcar tarefa como concluída \n4 Remover tarefa \n5 Editar tarefa\n6 Sair do programa")
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

