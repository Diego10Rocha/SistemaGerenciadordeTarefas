class TaskDAO:
	def insertTask(self):
		task = [self.id_task, self.titulo, self.descricao, self.prioridade]
		with open("Tarefas.json", "ab") as arquivo:
			arquivo.write('{"'+self.titulo+'":"'+task+'"}'+'\n')
	
	def getDicTask():
		dictask = {}
		try:
			with open("Tarefas.txt", "rb") as arquivo:
				taskjson = arquivo.read()
				dictask = json.loads(taskjson)
				return dictask
		except:
			return 0