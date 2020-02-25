from hashlib import sha512
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
def TableTask(nickname, taskdao, dicttasks):
	tasks = PrettyTable(["Id", "Título", "Descrição", "Prioridade"])
	qtdIds = taskdao.getUltimoId(nickname)

	# Alinha as colunas
	tasks.align["Id"] = "l"
	tasks.align["Título"]="l"
	tasks.align["Descrição"] = "l"
	tasks.align["Prioridade"] = "l"

	numprioridade = ""
	for i in range(3):
		for j in range(qtdIds):
			values_dict= dicttasks.get(str(i+1)+str(j+1), "")
			if(values_dict):
				numprioridade = values_dict[3]
				idtask = values_dict[0]
				titulo_task = values_dict[1]
				descricao_task = values_dict[2]

			if(numprioridade == "1"):
				strprioridade = "Alta"
			elif(numprioridade == "2"):
				strprioridade = "Média"
			elif(numprioridade == "3"):
				strprioridade = "Baixa"

			if(values_dict):
				tasks.add_row([idtask, titulo_task, descricao_task, strprioridade])
	return tasks
