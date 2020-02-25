import json
from pickle import *
class TaskDAO:
	#Bloco de código para inserir uma tarefa
	def insertTask(self):
		chave = self.prioridade+ str(self.id_task)
		dictTask = "{\""+chave+"\": [\""+str(self.id_task)+"\",\""+ self.titulo+"\",\""+ self.descricao+"\",\""+ self.prioridade+"\"]}"
		dictKeys = "{\""+str(self.id_task)+"\": \""+str(self.id_task)+"\"}"
		with open("Tasks/"+self.user+".user", "ab") as file:
			dump(dictTask, file)
		with open("Tasks/"+self.user+".id", "ab") as file:
			dump(dictKeys, file)

	#Bloco de código paraa pegar as tarefas do usuário logado no sistema e inserir num dicionário
	def getDicTask(nick):
		maptasks = {}
		try:
			with open("Tasks/"+nick+".user", 'rb') as file:
				while True:
					try:
						task = load(file)
						dicttask = json.loads(task)
						for chave, valor in dicttask.items():
							maptasks[chave] = valor
					except EOFError:
						break
			return maptasks
		except:
			print("Not found")
			return maptasks

	#Bloco de código para pegar o ultimo Id atribuído a uma tarefa de determinado usuário
	def getUltimoId(nick):
		maptasks = {}
		try:
			with open("Tasks/"+nick+".id", 'rb') as file:
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

	#Bloco de código para alterar e para excluir as tarefas de um usuário
	def DeleteUpdate(dictTask, nickname):
		with open("Tasks/"+nickname+".user", "wb") as arquivo:
			for chave, valor in dictTask.items():
				newDicTask = "{\""+chave+"\": [\""+valor[0]+"\",\""+valor[1]+"\",\""+valor[2]+"\",\""+valor[3]+"\"]}"
				dump(newDicTask, arquivo)
