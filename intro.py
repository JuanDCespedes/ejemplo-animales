class Animal:
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza
    def pasear(self):
        pass
    def alimentar(self):
        pass
    def dar_info(self):
        return self.nombre + " de raza: " + self.raza
class Mascota(Animal):
    def __init__(self, nombre, raza, propietario):
        super.__init__(super(type(nombre), type(raza)))
        self.nombre=nombre
        self.raza=raza
        self.propietario=propietario
class Gato(Mascota):
    def pasear(self):
        print("paseando al gato " + self.dar_info()+" "+self.propietario)

    def alimentar(self):
        print ("alimentando al gato "+self.dar_info()+" "+self.propietario)
class Perro(Mascota):
    def pasear(self):
        print("paseando al perro "+self.dar_info()+" "+self.propietario)
    def alimentar(self):
        print("alimentando al perro " +self.dar_info()+" "+self.propietario)
class Lagarto(Mascota):
    def pasear(self):
        print("paseando al lagarto "+self.dar_info()+" "+self.propietario)
    def alimentar(self):
        print("alimentado al lagarto "+self.dar_info()+" "+self.propietario)
if __name__ =="__main__":
    mascotas =[Perro("neron", "bulldog", "Juan"),Gato("fifi","angora", "Maria"), Lagarto("nextor", "verde no c xd", "Splinter")]
    for m in mascotas:
        m.pasear()
        m.alimentar()