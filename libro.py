class Libro:
    def __init__(self, titulo="", autor="", publicacion=0, editorial="" ):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicacion = publicacion
        self.__editorial = editorial

    def __str__(self): 
        return (
            'Titulo: ' + self.__titulo + '\n' +
            'Autor: ' + self.__autor + '\n' +
            'Publicado: ' + str(self.__publicacion) + '\n' +
            'Editorial: ' + self.__editorial + '\n')   

#l01 = Libro(titulo="Programacion", autor="Deitel", publicacion=2020, editorial="Pearson")
#print(l01)
#l02 = Libro("Python", "Guido", "2010", "Planeta")
#print(l02)

