import json
class UserDAO:
	#Bloco de código para cadastrar um usuário
	def insertUser(self):
		with open("usuarios.txt", "a", encoding="UTF-8") as arquivo:
			if(UserDAO.getDicUser("")):
				arquivo.write(',"'+self.login+'":"'+self.password+'"')
			else:
				arquivo.write('"'+self.login+'":"'+self.password+'"')

	#Bloco de código pra pegar os usuários cadastrados e inserir em um dicionário
	def getDicUser(self):
		dicusers = {}
		try:
			with open("usuarios.txt", "r", encoding="UTF-8") as arquivo:
				userjson = arquivo.read()
				userjson = '{'+userjson+'}'
				dicusers = json.loads(userjson)
				return dicusers
		except:
			return dicusers

	#Bloco de código para efetuar o login de um usuário
	def login(nick, password):
		users = UserDAO.getDicUser("")
		userverify = users.get(nick, False)
		if(userverify == password):
			return True
		else:
			input("Usuário e/ou senha incorreto(s).\nAperte enter para voltar ao menu.")
			return False
