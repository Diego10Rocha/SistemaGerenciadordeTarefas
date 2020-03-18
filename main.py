'''
******************************************************************************************
Autor: Fulano de Tal
Componente Curricular: Algoritmos I
Concluido em: 14/10/2011
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''


from User import User
from Task import Task
import os

from funcoes import PegarOpcaoDoMenu, CriptografarSenha, getUltimoId, OrdenaTask

option = 0

while(option != 3):
    os.system('cls' if os.name == 'nt' else 'clear')
    option = PegarOpcaoDoMenu(3)
    usersingularity = False

    #Bloco de código para cadastrar um usuário
    if(option == 1):
        usersexists = False
        users = User.getDicUser("")
        boolsingularity = False
        if(users):
            usersexists = True

        contador=0
        #Bloco de código para verificar se o nickname desejado pelo usuario ainda não foi utilizado
        while(usersexists and not usersingularity):
            usersingularity = True
            boolsingularity = True
            charforbidden = False
            if(contador==0):
                nickname = input("Digite seu nickname\n")
            else:
                nickname = input("Nickname em uso. Por favor escolha outro nickname.\n")
            contador+=1
            for i in range(len(nickname)):
                if(nickname[i] == "/" or nickname[i] == '\\'):
                    charforbidden = True
            while(nickname == "" or charforbidden):
                charforbidden = False
                nickname = input("Seu nickname não pode ser vazio nem conter os caracteres '/ e \ ', digite novamente\n")
                for i in range(len(nickname)):
                    if(nickname[i] == "/" or nickname[i] == '\\'):
                        charforbidden = True
            for elemento in users:
                if(elemento == nickname):
                    usersingularity = False
                    break

        if(not boolsingularity):
            charforbidden = False
            nickname = input("Digite seu nickname\n")
            for i in range(len(nickname)):
                if(nickname[i] == "/" or nickname[i] == '\\'):
                    charforbidden = True
            while(nickname == "" or charforbidden):
                charforbidden = False
                nickname = input("Seu nickname não pode ser vazio nem conter os caracteres '/ e \ ', digite novamente\n")
                for i in range(len(nickname)):
                    if(nickname[i] == "/" or nickname[i] == '\\'):
                        charforbidden = True

        password = input("Digite sua senha\n")
        hashpass = CriptografarSenha(password)

        user = User(nickname, hashpass)
        user.insertUser()

    #Bloco de código para o login de um usuário
    elif(option == 2):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("#"*22)
        print("#       Login        #")
        print("#"*22)

        nickname = input("Digite seu nickname:\n")
        password = input("Digite sua senha:\n")
        hashpass = CriptografarSenha(password)
        user = User(nickname, hashpass)

        os.system('cls' if os.name == 'nt' else 'clear')
        boollog = user.loginUser()

        #Se o usuário conseguir logar, o submenu relacionado a tarefas é mostrado
        if(boollog):
            dicttasks = Task.getDicTask(Task, user.login)
            OrdenaTask(user, dicttasks)
            while True:
                option = PegarOpcaoDoMenu(5)

                #Bloco de código para cadastrar uma tarefa
                if(option == 1):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("#" * 26)
                    print("#   Cadastro de tarefas  #")
                    print("#" * 26)
                    while True:
                        titulo = input("Digite o titulo da tarefa:\n")
                        if(titulo!=""):
                            break
                    while True:
                        descricao = input("Digite a descrição da tarefa:\n")
                        if(descricao!=""):
                            break
                    prioridade = ""
                    while(prioridade!="1" and prioridade!="2" and prioridade!="3"):
                        prioridade = input("Digite a prioridade da tarefa:\n1- Alta \n2- Média \n3- Baixa\n")

                    os.system('cls' if os.name == 'nt' else 'clear')
                    ultimoId = getUltimoId(user.login)
                    id_task = ultimoId+1
                    task = Task(titulo, descricao, prioridade, id_task, user.login)
                    task.insertTask(user)

                #Bloco de código para visualizar as tarefas do usuário logado
                elif(option == 2):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dicttasks = Task.getDicTask(Task, user.login)
                    if(dicttasks):
                        tasks = OrdenaTask(user, dicttasks)
                        print(tasks)
                    else:
                        print("Não há tarefas cadastradas")
                    input("Aperte enter para voltar ao menu de tarefas.")
                    os.system('cls' if os.name == 'nt' else 'clear')

                #Bloco de código para alterar informações das tarefas do usuário
                elif(option == 3):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dicttasks = Task.getDicTask(Task, user.login)
                    info_alterar = ""
                    if(dicttasks):
                        tasks = OrdenaTask(user, dicttasks)
                        print(tasks)
                        id_edit = input("Digite o Id da tarefa que deseja editar: ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if(dicttasks.get("1"+str(id_edit), "") or dicttasks.get("2"+str(id_edit), "") or dicttasks.get("3"+str(id_edit), "")):
                            while(info_alterar!="1" and info_alterar!="2" and info_alterar!="3"):
                                info_alterar = input("Digite a informação que deseja alterar:\n1-Titulo\n2-Descrição\n3-Prioridade\n")
                            if(info_alterar == "1"):
                                new_title = input("Digite o novo titulo:\n")
                                if(dicttasks.get("1"+id_edit, "")):
                                    dicttasks["1" + id_edit].titulo = new_title
                                elif(dicttasks.get("2"+id_edit, "")):
                                    dicttasks["2"+id_edit].titulo = new_title
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit].titulo = new_title
                                Task.DeleteOrUpdate(dicttasks, nickname)
                            elif(info_alterar == "2"):
                                new_desc = input("Digite a nova descrição:\n")
                                if(dicttasks.get("1"+id_edit, "")):
                                    dicttasks["1"+id_edit].descricao = new_desc
                                elif(dicttasks.get("2"+id_edit, "")):
                                    dicttasks["2"+id_edit].descricao = new_desc
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit].descricao = new_desc
                                Task.DeleteOrUpdate(dicttasks, nickname)
                            elif(info_alterar == "3"):
                                new_priorirty = ""
                                while(new_priorirty!="1" and new_priorirty!="2" and new_priorirty!="3"):
                                    new_priorirty = input("Digite qual a nova prioridade:\n1-Alta\n2-Média\n3-Baixa\n")
                                if(dicttasks.get("1" + id_edit, "")):
                                    dicttasks["1" + id_edit].prioridade = new_priorirty
                                    dicttasks[new_priorirty + id_edit] = dicttask["1"+id_edit]
                                    del dicttasks["1"+id_edit]
                                elif(dicttasks.get("2" + id_edit, "")):
                                    dicttasks["2"+id_edit].prioridade = new_priorirty
                                    dicttasks[new_priorirty + id_edit] = dicttasks["2"+id_edit]
                                    del dicttasks["2"+id_edit]
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit].prioridade = new_priorirty
                                    dicttasks[new_priorirty + id_edit] = dicttasks["3"+id_edit]
                                    del dicttasks["3"+id_edit]
                                os.system('cls' if os.name == 'nt' else 'clear')
                                Task.DeleteOrUpdate(Task, dicttasks, nickname)
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("O Id informado não existe!")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Não há tarefas cadastradas!")
                        input("Aperte enter para continuar.")

                #Bloco de código para excluir as tarefas do usuário logado
                elif(option == 4):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dicttasks = Task.getDicTask(Task, user.login)
                    if(dicttasks):
                        tasks = OrdenaTask(user, dicttasks)
                        print(tasks)
                        id_excluir = input("Digite o Id da tarefa que deseja excluir: ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        dicttask = Task.getDicTask(Task, user.login)

                        if(dicttask.get("1"+id_excluir, "")):
                            del dicttask["1"+id_excluir]
                            Task.DeleteOrUpdate(Task, dicttask, nickname)
                        elif(dicttask.get("2"+id_excluir, "")):
                            del dicttask["2"+id_excluir]
                            Task.DeleteOrUpdate(Task, dicttask, nickname)
                        elif(dicttask.get("3"+id_excluir, "")):
                            del dicttask["3"+id_excluir]
                            Task.DeleteOrUpdate(Task, dicttask, nickname)
                        else:
                            print("O Id informado não existe!")
                            input("Aperte enter para voltar ao menu de tarefas")
                    else:
                        print("Não há tarefas cadastradas!!")

                #Bloco de código para fazer o logout do usuário
                elif(option == 5):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    option = PegarOpcaoDoMenu(3)
                    break
