class Persona:
    def inicializar(self,nombre):
        self.nombre = nombre
        
    def imprimir(self):
        print(f"Su nombre es: {self.nombre}")
print("============Persona numero 1============")        
persona1 = Persona()
persona1.inicializar("Gael")
persona1.imprimir()

print("================================================================")

print("============Persona numero 2============")
persona2 = Persona()
persona2.inicializar("Morin")
persona2.imprimir()
