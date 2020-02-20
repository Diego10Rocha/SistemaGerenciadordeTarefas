from funcoes import *
from User import User
from UserDAO import UserDAO
from TaskDAO import TaskDAO
opcao=0

while(opcao != 3):
	opcao = PegarOpcaoDoMenu(3)
	usersingularity = True

	if(opcao == 1):
		usersexists = False
		userdao = UserDAO
		users = userdao.getDicUser()
		boolsingularity = False
		if(users):
			usersexists = True
				
		while(usersexists and usersingularity):
			usersingularity = False
			nickname = input("Digite seu nickname\n")
			while(nickname==""):
				nickname = input("Seu nickname não pode ser vazio\n")
			if(users):
				for elemento in users:
					if(elemento == nickname):
						usersingularity = True
						boolsingularity = True
						break
			if(not usersingularity):
				boolsingularity = False
				break

		if(not usersingularity):
			nickname = input("Digite seu nickname\n")

		password = input("Digite sua senha\n")
		hashpass = CriptografarSenha(password)

		user = User(nickname, hashpass)
		userdao.insertUser(user)

	elif(opcao == 2):
		userdao = UserDAO
		taskdao = TaskDAO
		
		nickname = input("Digite seu nickname\n")
		password = input("Digite sua senha\n")
		hashpass = CriptografarSenha(password)

		boollog = userdao.login(nickname, hashpass)
		if(boollog):
			opcao = PegarOpcaoDoMenu(5)
			while True:
				opcao = PegarOpcaoDoMenu(5)
				
				if(opcao == 1):
					titulo = input("Digite o titulo da tarefa")
					descricao = input("Digite a descrição da tarefa")
					prioridade = ""
					while(prioridade!="1" and prioridade!="2" and prioridade!="3"):
						prioridade = input("Digite a prioridade da tarefa:\n1- Alta \n2-Média \n3- Baixa")

					id_task = taskdao.getDicTask()
					task = Task(id_task, titulo, descricao, prioridade)
					taskdao.insertTask(task)

				elif(opcao == 2):
					print("opcao 2")

				elif(opcao == 3):
					print("opcao 3")
				
				elif(opcao ==4 ):
					print("opcao 4")

				elif(opcao == 5):
					opcao = PegarOpcaoDoMenu(3)
					break
























'''
#Cria o arquivo
arquivo = open("usuarios.txt", "w")
arquivo.write("Diego")
arquivo.write("José")
arquivo.close()

#Ecreve no arquivo
arquivo = open("usuarios.txt", "a")
arquivo.write("\nDaniel\n")
arquivo.write("Artur")
arquivo.close()

arquivo = open("usuarios.txt", "a")
for i in range(10):
	usuario = input("Digite seu nickname")
	usuario = usuario + "\n"
	arquivo.write(usuario)
arquivo.close()'''
'''
#Lê o arquivo
arquivo = open("usuarios.txt", "r")
usuarios = []
for linha in arquivo:
	linha = linha.strip()
	usuarios.append(linha)
#print(arquivo.read())
#linha = arquivo.readline()
print(usuarios)
arquivo.close()

#O comando "with" fica responsável por fechar o arquivo após as operações terem sido terminadas
with open('usuarios.txt') as arquivo:
	for linha in arquivo:
		print(linha)



print("    _______________     ")
print("   /               \ ")
print("  /                 \ ")
print("//                   \/\ ")
print("\|      XXXX XXXX    | / ")
print(" |      XXXX XXXX    |/ ")
print(" |      XXX XXX      | ")
print(" |                   | ")
print(" \__      XXX      __/ ")
print("   |\     XXX     /| ")
print("   | |           | | ")
print("   | I I I I I I I | ")
print("   |  I I I I I I  | ")
print("    \_           _/ ")
print(" 	 \_     	_/ ")
print(" 	   \_______/ ")
'''