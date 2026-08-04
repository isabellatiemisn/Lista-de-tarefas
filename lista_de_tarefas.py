import json
import datetime
tarefas:str = []
categorias:str = []
acao: int = 0
c: int = 0
nova_tarefa: str = ""
def carregar (tarefas,categorias):   
    try:
        with open("ListaTarefas.json", "r") as arquivo:
            dados = json.load(arquivo)
            tarefas = dados.get("tarefas", [])
            categorias = dados.get("categorias", [])
        print ("Lista já existente")
        while (True): 
            try:
                arquivo = int(input("Deseja: 1 Manter lista ou 2 Criar nova lista? "))
                if (arquivo==1):
                    return tarefas, categorias
                elif(arquivo==2):
                    tarefas = []
                    categorias = []
                    return tarefas,categorias
                else:
                    print("Escolha uma opção válida")
            except: 
                print ("ERRO Digite o número de uma das opções")
    except:            
        with open ("ListaTarefas.json","w") as arquivo:
            dados = {"tarefas":tarefas,"categorias":categorias}
            json.dump(dados, arquivo)
            return tarefas, categorias

def salvar(tarefas,categorias):
    with open ("ListaTarefas.json","w") as arquivo:
        dados = {"tarefas":tarefas,"categorias":categorias}
        json.dump(dados, arquivo)

def criar(tarefas,categorias):
    while (True):
        nova_tarefa = str(input("Adicione uma tarefa (ou 'sair' para voltar):"))
        if (nova_tarefa == "sair"):
            break
        else:
            while(True):
                if not (len(categorias)==0):
                    texto = "Escolha uma categoria existente pelo número,\ncrie uma nova ou deixe em branco para não categorizar: "
                    for indice, categoria in enumerate(categorias, start=1):
                        print(str(indice) + " - " + categoria)
                else:
                    texto = "Nomeie uma categoria para a tarefa ou deixe em branco pra não categorizar: "
                entrada_categoria = input(texto)
                if((entrada_categoria=="0")or(entrada_categoria.strip() == "")):
                    categoria_escolhida = "Sem categoria"
                    break
                else:
                    try: 
                        numero = int(entrada_categoria)
                        numero = numero - 1
                        if (0 <= numero < len(categorias)):
                            categoria_escolhida = categorias[numero]
                            break
                        else:
                            print("ERRO Essa categoria não existe\nPor favor insira uma categoria válida")
                    except ValueError:
                        categoria_escolhida = entrada_categoria
                        categorias.append(categoria_escolhida)
                        break
        hoje = str(datetime.date.today())
        tarefas.append({"tarefa":nova_tarefa,"concluida":False,"categoria":categoria_escolhida,"data":hoje})
        
def listar(tarefas):
    print ("\n")
    if (len(tarefas)==0):
        print ("Sem Tarefas")
    else: 
        for indice, tarefa in enumerate(tarefas, start=1):
            if tarefa["concluida"]: 
                extra = " - Concluída"  
            else: 
                extra = " "
            print(str(indice) + " - " + tarefa["tarefa"] + " - " + "(" + tarefa["categoria"] + ")" + " - " + tarefa["data"] + extra )

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

tarefas, categorias = carregar (tarefas,categorias)
while (acao!=6):
