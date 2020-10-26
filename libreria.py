from libro import Libro

class Libreria:
    def __init__(self):
        self.__libros = []

    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Libro):
         self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

l01 = Libro(titulo="Programacion", autor="Deitel", publicacion=2020, editorial="Pearson")
l02 = Libro("Python", "Guido", "2010", "Planeta")
libreria = Libreria() 
libreria.agregar_final(l01)
libreria.agregar_inicio(l02)
libreria.agregar_inicio(l01)
libreria.mostrar()
