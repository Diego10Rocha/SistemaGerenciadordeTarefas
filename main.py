from Task import Task
from funcoes import *
from User import User
from UserDAO import UserDAO
from TaskDAO import TaskDAO
option = 0

while(option != 3):
    option = PegarOpcaoDoMenu(3)
    usersingularity = True

    if(option == 1):
        usersexists = False
        userdao = UserDAO
        users = userdao.getDicUser("")
        boolsingularity = False
        if(users):
            usersexists = True

        while(usersexists and usersingularity):
            usersingularity = False
            boolsingularity = True
            nickname = input("Digite seu nickname\n")
            while(nickname==""):
                nickname = input("Seu nickname não pode ser vazio, digite novamente\n")
            if(users):
                for elemento in users:
                    if(elemento == nickname):
                        usersingularity = True
                        break
            if(not usersingularity):
                boolsingularity = False
                break

        if(not boolsingularity):
            nickname = input("Digite seu nickname\n")
            while(nickname==""):
                nickname = input("Seu nickname não pode ser vazio, digite novamente\n")

        password = input("Digite sua senha\n")
        hashpass = CriptografarSenha(password)

        user = User(nickname, hashpass)
        userdao.insertUser(user)

    elif(option == 2):
        userdao = UserDAO
        taskdao = TaskDAO

        nickname = input("Digite seu nickname\n")
        password = input("Digite sua senha\n")
        hashpass = CriptografarSenha(password)

        boollog = userdao.login(nickname, hashpass)
        if(boollog):
            while True:
                option = PegarOpcaoDoMenu(5)

                if(option == 1):
                    titulo = input("Digite o titulo da tarefa")
                    descricao = input("Digite a descrição da tarefa")
                    prioridade = ""
                    while(prioridade!="1" and prioridade!="2" and prioridade!="3"):
                        prioridade = input("Digite a prioridade da tarefa:\n1- Alta \n2-Média \n3- Baixa")

                    id_task = taskdao.getDicTask()
                    task = Task(id_task, titulo, descricao, prioridade)
                    taskdao.insertTask(task)

                elif(option == 2):
                    print("opcao 2")

                elif(option == 3):
                    print("opcao 3")

                elif(option == 4):
                    print("opcao 4")

                elif(option == 5):
                    option = PegarOpcaoDoMenu(3)
                    break
