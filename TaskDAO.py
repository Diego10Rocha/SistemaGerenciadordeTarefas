import json
from pickle import *
from funcoes import *
import os


class TaskDAO:
    # Bloco de código para inserir uma tarefa
    def insertTask(self, user):
        dir = "./Tasks"
        try:
            os.mkdir(dir)
        except:
            pass
        key = self.prioridade + str(self.id_task)
        dicttask = {key: self}
        dictKeys = "{\"" + str(self.id_task) + "\": \"" + str(self.id_task) + "\"}"
        with open("Tasks/" + self.user + ".user", "ab") as file:
            dump(dicttask, file)
        with open("Tasks/" + self.user + ".id", "ab") as file:
            dump(dictKeys, file)
        print("Tarefa cadastrada!")
        dicttask = TaskDAO.getDicTask(user.login)
        OrdenaTask(user, TaskDAO, dicttask)

    # Bloco de código paraa pegar as tarefas do usuário logado no sistema e inserir num dicionário
    def getDicTask(nick):
        maptasks = {}
        task = {}
        try:
            with open("Tasks/" + nick + ".user", 'rb') as file:
                while True:
                    try:
                        task = load(file)
                        for key, value in task.items():
                            maptasks[key] = value
                    except EOFError:
                        break
            return maptasks
        except:
            print("Not found")
            return maptasks

    # Bloco de código para pegar o ultimo Id atribuído a uma tarefa de determinado usuário
    def getUltimoId(nick):
        maptasks = {}
        try:
            with open("Tasks/" + nick + ".id", 'rb') as file:
                while True:
                    try:
                        task = load(file)
                        dicttask = json.loads(task)
                        for chave, valor in dicttask.items():
                            maptasks[chave] = valor
                    except EOFError:
                        break
            ultimo_id = len(maptasks)
            return ultimo_id
        except:
            ultimo_id = len(maptasks)
            return ultimo_id

    # Bloco de código para alterar e para excluir as tarefas de um usuário
    def DeleteUpdate(dictTask, nickname):
        with open("Tasks/" + nickname + ".user", "wb") as arquivo:
            for key, value in dictTask.items():
                newDicTask = {key : value}
                dump(newDicTask, arquivo)
        print("Operação realizada com sucesso!")
        input("Aperte enter para voltar ao menu de tarefas.")
