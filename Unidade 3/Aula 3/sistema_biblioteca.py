class Livro:
    def __init__(self, titulo:str, genero:list, autor:str, isbn:str, editora:str, estaDisponivel:bool ):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.isbn = isbn
        self.editora = editora
        self.estaDisponivel = estaDisponivel
    
    def alternarStatus(self):
        self.estaDisponivel = not self.estaDisponivel


class Usuario:
    def __init__(self, nome:str, senha:str, email:str):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.lista_livros = []
    
    def receber_livro(self, livro):
        self.lista_livros.append(livro)

    def devolver_livro(self, livro):
        self.lista_livros.remove(livro)

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_livros = []
        self.lista_usuarios = []
    
    def cadastrar_livro(self, livro:Livro):
        self.lista_livros.append(livro)

    def cadastrar_usuario(self, usuario:Usuario):
        self.lista_usuarios.append(usuario)
    
    def emprestar_livro(self, livro:Livro, usuario:Usuario):
        if livro.estaDisponivel:
            livro.alternarStatus()
            usuario.receber_livro(livro)
    
    def receber_livro(self, livro:Livro, usuario:Usuario):
        if livro in usuario.lista_livros:
            livro.alternarStatus()
            usuario.devolver_livro()

    
biblioteca = Biblioteca("Biblioteca Senac")
livro1 = Livro("Crônicas de Nárnia", ["Ficção","Aventura"], "Lewis", "123", "Globo", True)
usuario1 = Usuario("Carlos", "123456", "carlos@gmail.com")

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_usuario(usuario1)
biblioteca.emprestar_livro(livro1, usuario1)
print(livro1.estaDisponivel)
print(usuario1.lista_livros[0].titulo)