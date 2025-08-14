class Libro:
    def __init__(self, titulo,autor,a_publicacion,cod_unico):
        self.titulo = titulo
        self.autor = autor
        self.a_publicacion = a_publicacion
        self.cod_unico = cod_unico

class Usuario:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera


class Gestor_Libros:
    def __init__(self):
        self.libros = {}
    def registrar_libro(self, titulo, autor, a_publicacion, cod_unico):
        if cod_unico in self.libros:
            raise ValueError("Codigo de libro ya registrado")
        self.libros[cod_unico] = Libro(titulo,autor,a_publicacion,cod_unico)
    def buscar_libro(self, cod_unico):
        return self.libros.get(cod_unico)
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros registrados")
            for libro in self.libros.values():
                estado="Disponible" if libro.disponible else "No Disponible"
                print(f"{libro.cod_unico} - {libro.titulo} - {estado}")
class Gestor_Usuarios:
    def __init__(self):
        self.usuarios = {}
    def registrar_usuario(self, nombre, carnet, carrera):
        if carnet in self.usuarios:
            raise ValueError("Carnet ya registrado")
        self.usuarios[carnet] = Usuario(nombre, carnet, carrera)
    def buscar_usuario(self, carnet):
        return self.usuarios.get(carnet)
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
            for usuario in self.usuarios.values():
                print(f"{usuario.nombre} - {usuario.carnet} - {usuario.carrera}")
class Gestor_Prestamos:
