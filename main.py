from Task import Task
from funcoes import *
from User import User
from UserDAO import UserDAO
from TaskDAO import TaskDAO

option = 0

while(option != 3):
    option = PegarOpcaoDoMenu(3)
    usersingularity = False

    #Bloco de código para cadastrar um usuário
    if(option == 1):
        usersexists = False
        userdao = UserDAO
        users = userdao.getDicUser("")
        boolsingularity = False
        if(users):
            usersexists = True

        #Bloco de código para verificar se o nickname desejado pelo usuario ainda não foi utilizado
        while(usersexists and not usersingularity):
            usersingularity = True
            boolsingularity = True
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
        userdao.insertUser(user)

    #Bloco de código para o login de um usuário
    elif(option == 2):
        userdao = UserDAO
        taskdao = TaskDAO

        nickname = input("Digite seu nickname\n")
        password = input("Digite sua senha\n")
        hashpass = CriptografarSenha(password)

        boollog = userdao.login(nickname, hashpass)
        #Se o usuário conseguir logar, o submenu relacionado a tarefas é mostrado
        if(boollog):
            while True:
                option = PegarOpcaoDoMenu(5)

                #Bloco de código para cadastrar uma tarefa
                if(option == 1):
                    titulo = input("Digite o titulo da tarefa")
                    descricao = input("Digite a descrição da tarefa")
                    prioridade = ""
                    while(prioridade!="1" and prioridade!="2" and prioridade!="3"):
                        prioridade = input("Digite a prioridade da tarefa:\n1- Alta \n2-Média \n3- Baixa")

                    ultimoId = taskdao.getUltimoId(nickname)
                    id_task = ultimoId+1
                    task = Task(titulo, descricao, prioridade, id_task, nickname)
                    taskdao.insertTask(task)

                #Bloco de código para visualizar as tarefas do usuário logado
                elif(option == 2):
                    dicttasks = taskdao.getDicTask(nickname)
                    if(dicttasks):
                        tasks = TableTask(nickname, taskdao, dicttasks)
                        print(tasks)
                    else:
                        print("Não há tarefas cadastradas")

                #Bloco de código para alterar informações das tarefas do usuário
                elif(option == 3):
                    dicttasks = taskdao.getDicTask(nickname)
                    info_alterar = ""
                    if(dicttasks):
                        tasks = TableTask(nickname, taskdao, dicttasks)
                        print(tasks)
                        id_edit = input("Digite o Id da tarefa que deseja editar: ")
                        if(dicttasks.get("1"+str(id_edit), "") or dicttasks.get("2"+str(id_edit), "") or dicttasks.get("3"+str(id_edit), "")):
                            while(info_alterar!="1" and info_alterar!="2" and info_alterar!="3"):
                                info_alterar = input("Digite a informação que deseja alterar:\n1-Titulo\n2-Descrição\n3-Prioridade\n")
                            if(info_alterar == "1"):
                                new_title = input("Digite o novo titulo")
                                if(dicttasks.get("1"+id_edit, "")):
                                    dicttasks["1"+id_edit][1] = new_title
                                elif(dicttasks.get("2"+id_edit, "")):
                                    dicttasks["2"+id_edit][1] = new_title
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit][1] = new_title
                                taskdao.DeleteUpdate(dicttasks, nickname)
                            elif(info_alterar == "2"):
                                new_desc = input("Digite a nova descrição")
                                if(dicttasks.get("1"+id_edit, "")):
                                    dicttasks["1"+id_edit][2] = new_desc
                                elif(dicttasks.get("2"+id_edit, "")):
                                    dicttasks["2"+id_edit][2] = new_desc
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit][2] = new_desc
                                taskdao.DeleteUpdate(dicttasks, nickname)
                            elif(info_alterar == "3"):
                                new_priorirty = input("Digite qual a nova prioridade:\n1-Alta\n2-Média\n3-Baixa")
                                if(dicttasks.get("1"+id_edit, "")):
                                    dicttasks["1"+id_edit][3] = new_priorirty
                                elif(dicttasks.get("2"+id_edit, "")):
                                    dicttasks["2"+id_edit][3] = new_priorirty
                                elif(dicttasks.get("3"+id_edit, "")):
                                    dicttasks["3"+id_edit][3] = new_priorirty
                                taskdao.DeleteUpdate(dicttasks, nickname)
                            print("Tarefa alterada com sucesso!")
                        else:
                            print("O Id informado não existe!")
                    else:
                        print("Não há tarefas cadastradas")

                #Bloco de código para excluir as tarefas do usuário logado
                elif(option == 4):
                    dicttasks = taskdao.getDicTask(nickname)
                    tasks = TableTask(nickname, taskdao, dicttask)
                    print(tasks)
                    id_excluir = input("Digite o Id da tarefa que deseja excluir: ")
                    dicttask = taskdao.getDicTask(nickname)

                    if(dicttask.get("1"+id_excluir, "")):
                        del dicttask["1"+id_excluir]
                    elif(dicttask.get("2"+id_excluir, "")):
                        del dicttask["2"+id_excluir]
                    elif(dicttask.get("3"+id_excluir, "")):
                        del dicttask["3"+id_excluir]
                    taskdao.DeleteUpdate(dicttask, nickname)
                    print("Tarefa excluída!")

                #Bloco de código para fazer o logout do usuário
                elif(option == 5):
                    option = PegarOpcaoDoMenu(3)
                    break
