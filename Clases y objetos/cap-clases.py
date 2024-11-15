## Clases
# Definición
class Usuario:
    # Atributos
    def __init__(self, email, password, sueldo = 0):
        self.email = email
        self.password = password
        self.sueldo = sueldo
    # Métodos
    def calcularDesc(self, estima):
        hijos = estima * (1 + 0.0005 * self.sueldo)
        return hijos

# Modificar valores
Usuario.email = "angelmarin@unmsm.edu.pe"
Usuario.password = "********"

# Acceder valores
print(Usuario.email, Usuario.password)

# Crear objeto
testerUser = Usuario("admin@unmsm.edu.pe", "********")
print(testerUser.email)
print(testerUser.password)
print(testerUser)
print(id(testerUser))