import json
class UserDAO:

	def insertUser(self):
		with open("usuarios.txt", "a") as arquivo:
			if(UserDAO.getDicUser("")):
				arquivo.write(',"'+self.login+'":"'+self.password+'"')

			else:
				arquivo.write('"'+self.login+'":"'+self.password+'"')

	def getDicUser(self):
		try:
			with open("usuarios.txt", "r") as arquivo:
				userjson = arquivo.read()
				userjson = '{'+userjson+'}'
				dicusers = json.loads(userjson)
				return dicusers
		except:
			return ""

	def login(nick, password):
		users = {}
		users = UserDAO.getDicUser("")
		userverify = users.get(nick, False)
		if(userverify == password):
			print("Usuario logado!!")
			return True
		else:
			print("Usuário e/ou senha incorreto(s)")
			return False
