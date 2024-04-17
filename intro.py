class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Propietario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []
        self.productos = []

    def comprar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"{self.nombre} ha comprado una mascota: {mascota.nombre}")

    def comprar_producto(self, producto):
        self.productos.append(producto)
        print(f"{self.nombre} ha comprado un producto: {producto.nombre}")

class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def dar_info(self):
        return f"{self.nombre} de raza: {self.raza}"

    def pasear(self):
        pass

    def alimentar(self):
        pass

class Mascota(Animal):
    def __init__(self, nombre, raza, propietario):
        super().__init__(nombre, raza)
        self.propietario = propietario
        propietario.comprar_mascota(self)

    def pasear(self):
        pass

    def alimentar(self):
        pass

class Gato(Mascota):
    def pasear(self):
        print("Paseando al gato " + self.dar_info() + " de " + self.propietario.nombre)

    def alimentar(self):
        print("Alimentando al gato " + self.dar_info() + " de " + self.propietario.nombre)

class Perro(Mascota):
    def pasear(self):
        print("Paseando al perro " + self.dar_info() + " de " + self.propietario.nombre)

    def alimentar(self):
        print("Alimentando al perro " + self.dar_info() + " de " + self.propietario.nombre)

class Lagarto(Mascota):
    def pasear(self):
        print("Paseando al lagarto " + self.dar_info() + " de " + self.propietario.nombre)

    def alimentar(self):
        print("Alimentando al lagarto " + self.dar_info() + " de " + self.propietario.nombre)

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []
        self.productos = []

    def vender_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"{self.nombre} ha vendido una mascota: {mascota.nombre}")

    def vender_producto(self, producto):
        self.productos.append(producto)
        print(f"{self.nombre} ha vendido un producto: {producto.nombre}")

if __name__ == "__main__":
    tienda = Tienda("Mi Tienda")

    propietario1 = Propietario("Juan")
    tienda.vender_mascota(Perro("Neron", "bulldog", propietario1))
    tienda.vender_producto(Producto("Hueso", 5))

    propietario2 = Propietario("Maria")
    tienda.vender_mascota(Gato("Fifi", "angora", propietario2))
    tienda.vender_producto(Producto("Arena para gatos", 10))
    
    propietario3 = Propietario("Splinter")
    tienda.vender_mascota(Lagarto("Nextor", "verde no c xd", propietario3))
    tienda.vender_producto(Producto("Calentador para terrario", 20))

    print("Mascotas de la tienda:")
    for mascota in tienda.mascotas:
        print(mascota.dar_info())

    print("\nProductos de la tienda:")
    for producto in tienda.productos:
        print(f"Producto: {producto.nombre}, Precio: {producto.precio}")