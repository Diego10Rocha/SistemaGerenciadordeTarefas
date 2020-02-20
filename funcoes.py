from hashlib import sha512

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

def CriptografarSenha(senha):
	hash=sha512()
	hash.update(senha.encode('utf-8'))
	hashpass=hash.hexdigest()
	return hashpass