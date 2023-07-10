from Preentrega.PreEntrega2 import Cliente

clientes = []  

while True:
    nombre = input("Ingrese el nombre del cliente (o 'salir' para salir): ")
    if nombre == 'salir':
        break

    email = input("Ingrese el email del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    while True:
       telefono = input("Ingrese el teléfono del cliente: ")
       if telefono.isdigit():
                break
       else:
            print("El teléfono debe ser numérico. Inténtelo nuevamente.")

    cliente = Cliente(nombre, email, direccion, telefono)
    clientes.append(cliente)


print("Clientes ingresados:")
for cliente in clientes:
    print(cliente)