from pickle import *
from funcoes import *
import os

class Task:
	def __init__(self, titulo, descricao, prioridade, id_task, user):
		self.titulo = titulo
		self.descricao = descricao
		self.prioridade = prioridade
		self.id_task = id_task
		self.user = user

	# Bloco de código para inserir uma tarefa
	def insertTask(self, user):
		dir = "./Tasks"
		try:
			os.mkdir(dir)
		except:
			pass
		key = self.prioridade + str(self.id_task)
		dicttask = {key: self}
		dictKeys = {str(self.id_task): str(self.id_task)}
		with open("Tasks/" + self.user + ".user", "ab") as file:
			dump(dicttask, file)
		with open("Tasks/" + self.user + ".id", "ab") as file:
			dump(dictKeys, file)
		print("Tarefa cadastrada!")
		dicttask = self.getDicTask(user.login)
		OrdenaTask(user, dicttask)

	# Bloco de código paraa pegar as tarefas do usuário logado no sistema e inserir num dicionário
	def getDicTask(self, nick):
		maptasks = {}
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
			return maptasks


	# Bloco de código para alterar e para excluir as tarefas de um usuário
	def DeleteOrUpdate(self, dictTask, nickname):
		with open("Tasks/" + nickname + ".user", "wb") as arquivo:
			for key, value in dictTask.items():
				newDicTask = {key : value}
				dump(newDicTask, arquivo)
		print("Operação realizada com sucesso!")
		input("Aperte enter para voltar ao menu de tarefas.")