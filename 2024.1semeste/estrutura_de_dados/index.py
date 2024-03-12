from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela





contatos = []

# FUNÇÕES
def AdicionarContato():
    # ESCREVER LÓGICA AQUI!
    nome = input("Digite o nome: ")
    numero = int(input("Digite o número: "))

    contatos.append({
         "nome" : nome,
         "numero" : numero
    })


    
    print("\n LISTA DE DICIONÁRIO")
    print(contatos)

    print("Usuário Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI
    print(contatos)
    print("Mostrando lista de contatos")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    busca_nome = input("Digite o Nome do contato que você deseja alterar: ")
    global contatos  
    # if busca_nome in contatos.keys():
    #     escolha = int(input("Digite 1 pra editar nome 2 para editar o número: "))
    for contato in contatos:
        if busca_nome == contato["nome"]:
            escolha = int(input("Digite 1 pra editar nome 2 para editar o número: "))
    
            if escolha == 1:
                busca_nome = input("Digite o nome do contato: ")
                if nome_editado:
                        contatos[nome_editado] = contatos.pop(busca_nome)

            elif escolha == 2: 
                    numero_editado = input("Atualize aqui o número: ")
                    contatos =[nome_editado] = numero_editado
                

    print("Contato editado com sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    
    destinatario = Contato("Contato para envio", "Numero para envio")
    mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    print("Mensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        MostrarContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")