from UserDAO import UserDAO
class User:
	def __init__(self, login, password):
		print("criando um usuario")
		self.login = login
		self.password = password
	