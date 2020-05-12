from hashlib import sha512
from pickle import load

from prettytable import PrettyTable

#Bloco de código para mostrar o menu e o submenu

def PegarOpcaoDoMenu(len_menu):
	while True:
		if(len_menu == 3):
			print("##################################")
			print("#            MENU                #")
			print("##################################")
			print("#  [1] - Cadastrar novo usuário  #")
			print("#  [2] - Logar no sistema        #")
			print("#  [3] - Sair do sistema         #")
			print("##################################")
		elif(len_menu == 5):
			print("#################################")
			print("#            MENU               #")
			print("#################################")
			print("#  [1] - Cadastrar nova Tarefa  #")
			print("#  [2] - Visualizar Tarefas     #")
			print("#  [3] - Alterar Tarefa         #")
			print("#  [4] - Excluir Tarefa         #")
			print("#  [5] - Sair                   #")
			print("#################################")
		try:
			opcao = int(input("Digite uma opção: "))
			if(opcao>0 and opcao<=len_menu):
				return opcao
		except:
			print("Opção inválida")

#Bloo de código para criptografar a senha dos usuários
def CriptografarSenha(senha):
	hash=sha512()
	hash.update(senha.encode('utf-8'))
	hashpass=hash.hexdigest()
	return hashpass
#Bloco de código para criar uma tabela com as tarefas de um usuário
def OrdenaTask(user, dicttasks):
	table_tasks = PrettyTable(["Id", "Título", "Descrição", "Prioridade"])
	qtdIds = getUltimoId(user.login)

	# Alinha as colunas
	table_tasks.align["Id"] = "l"
	table_tasks.align["Título"]="l"
	table_tasks.align["Descrição"] = "l"
	table_tasks.align["Prioridade"] = "l"

	numprioridade = ""
	for i in range(3):
		for j in range(qtdIds):
			task = dicttasks.get(str(i+1)+str(j+1), "")
			if(task):
				numprioridade = task.prioridade

			if(numprioridade == "1"):
				strprioridade = "Alta"
			elif(numprioridade == "2"):
				strprioridade = "Média"
			elif(numprioridade == "3"):
				strprioridade = "Baixa"

			if(task):
				table_tasks.add_row([task.id_task, task.titulo, task.descricao, strprioridade])
				user.tasks.append([task.id_task, task.titulo, task.descricao, strprioridade])
	return table_tasks

# Bloco de código para pegar o ultimo Id atribuído a uma tarefa de determinado usuário
def getUltimoId(nick):
	maptasks = {}
	try:
		with open("Tasks/" + nick + ".id", 'rb') as file:
			while True:
				try:
					task = load(file)
					for chave, valor in task.items():
						maptasks[chave] = valor
				except EOFError:
					break
		ultimo_id = len(maptasks)
		return ultimo_id
	except:
		ultimo_id = len(maptasks)
		return ultimo_id