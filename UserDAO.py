import json
class UserDAO:
	'''def getListUser():
		users = []
		try:
			with open("usuarios.txt", "r") as arquivo:
				if(arquivo):
					arquivo.read()
					for linha in arquivo:
						linha = linha.strip()
						usera.append(linha)
		except:
			print("O arquivo não existe!!")

		return users'''
	
	def insertUser(self):
		with open("usuarios.txt", "a") as arquivo:
			arquivo.write('{"'+self.login+'":"'+self.password+'"}'+'\n')
	
	def getDicUser():
		dicusers = {}
		try:
			with open("usuarios.txt", "r") as arquivo:
				userjson = arquivo.read()
				dicusers = json.loads(userjson)
				print(dicusers)
				return dicusers
		except:
			print("")
			
	def login(nick, password):
		users = {}
		users = UserDAO.getDicUser()
		print(users)
		userverify = users.get(nick, False)
		print(usersverify)
		if(userverify == password):
			print("Usuario logado!!")
			return True
		else:
			print("Usuário e/ou senha incorreto(s) ")
			return False