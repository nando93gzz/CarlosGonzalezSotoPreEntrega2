class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def realizar_compra(self, producto):
        pass

    def mostrar_informacion(self):
        pass

    def __str__(self):
        return self.nombre