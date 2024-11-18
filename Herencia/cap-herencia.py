
class Usuario:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # Método para imprimir del objeto con print()
    def __str__(self):
        return "Nombre de usuario: " + self.username + ", Correo electronico: " + self.email + ", Contraseña: " + self.password

class Administrador(Usuario):
    def __init__(self, username, email, password, sueldo):
        # Invocación al constructor padre
        super().__init__(username, email, password)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + ", Sueldo de Admin: " + str(self.sueldo)

userTester = Usuario("magno", "magno@correo.com", "contra123")
print(userTester)

adminTester = Administrador("legna", "legna@correo.com", "legna123", 4800.00)
print(adminTester)
