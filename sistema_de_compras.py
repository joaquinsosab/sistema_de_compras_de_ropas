class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaMujer

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.ropa_hombre = []
        self.ropa_mujer = []
    
    def agregar_prenda(self, prenda, tipo):
        if tipo == "hombre":
            self.ropa_hombre.append(prenda)
        elif tipo == "mujer":
            self.ropa_mujer.append(prenda)
    
    def mostrar_inventario_hombre(self):
        print("Inventario de Ropa de Hombre:")
        for i, prenda in enumerate(self.ropa_hombre, 1):
            print(f"{i}. ", end="")
            prenda.mostrar_info()
    
    def mostrar_inventario_mujer(self):
        print("Inventario de Ropa de Mujer:")
        for i, prenda in enumerate(self.ropa_mujer, 1):
            print(f"{i}. ", end="")
            prenda.mostrar_info()

class Carrito:
    def __init__(self):
        self.prendas = []

    def agregar_al_carrito(self, prenda, cantidad):
        self.prendas.append((prenda, cantidad))
    
    def mostrar_carrito(self):
        total = 0
        print("\nCarrito de Compras:")
        for i, (prenda, cantidad) in enumerate(self.prendas, 1):
            print(f"{i}. {prenda.nombre}, Precio: ${prenda.precio}, Cantidad: {cantidad}, Talla: {prenda.talla}")
            total += prenda.precio * cantidad
        print(f"Total: ${total}")

def menu(inventario, carrito):
    while True:
        print("\nMenú de Sistema de Compras de Ropa")
        print("1: Ver ropa de hombre")
        print("2: Ver ropa de mujer")
        print("3: Ver carrito")
        print("4: Confirmar compra")
        print("5: Cancelar compra y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            inventario.mostrar_inventario_hombre()
            print("Seleccione el número del producto que desea añadir al carrito: ")
            producto_index = int(input()) - 1
            if 0 <= producto_index < len(inventario.ropa_hombre):
                prenda_seleccionada = inventario.ropa_hombre[producto_index]
                print("Ingrese la cantidad: ")
                cantidad = int(input())
                if cantidad > 0 and cantidad <= prenda_seleccionada.cantidad:
                    carrito.agregar_al_carrito(prenda_seleccionada, cantidad)
                    print(f"{cantidad} unidades de {prenda_seleccionada.nombre} añadidas al carrito.")
                else:
                    print("Cantidad inválida.")
            else:
                print("Selección inválida.")
        elif opcion == '2':
            inventario.mostrar_inventario_mujer()
            print("Seleccione el número del producto que desea añadir al carrito: ")
            producto_index = int(input()) - 1
            if 0 <= producto_index < len(inventario.ropa_mujer):
                prenda_seleccionada = inventario.ropa_mujer[producto_index]
                print("Ingrese la cantidad: ")
                cantidad = int(input())
                if cantidad > 0 and cantidad <= prenda_seleccionada.cantidad:
                    carrito.agregar_al_carrito(prenda_seleccionada, cantidad)
                    print(f"{cantidad} unidades de {prenda_seleccionada.nombre} añadidas al carrito.")
                else:
                    print("Cantidad inválida.")
            else:
                print("Selección inválida.")
        elif opcion == '3':
            carrito.mostrar_carrito()
        elif opcion == '4':
            carrito.mostrar_carrito()
            print("Compra confirmada. ¡Gracias por su compra!")
            break
        elif opcion == '5':
            print("Compra cancelada. Saliendo del sistema.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalón = RopaHombre("Pantalón de Hombre", 30.00, 30, "M")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "M")
zapato = RopaHombre("Zapatos de Hombre", 60.00, 25, "9.5 US")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "M")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")
vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "M")
zapatos = RopaMujer("Zapatos de Mujer", 50.00, 20, "6 US")

inventario = Inventario()
inventario.agregar_prenda(camisa, "hombre")
inventario.agregar_prenda(pantalón, "hombre")
inventario.agregar_prenda(chaqueta, "hombre")
inventario.agregar_prenda(zapato, "hombre")
inventario.agregar_prenda(falda, "mujer")
inventario.agregar_prenda(blusa, "mujer")
inventario.agregar_prenda(vestido, "mujer")
inventario.agregar_prenda(zapatos, "mujer")

carrito = Carrito()
menu(inventario, carrito)