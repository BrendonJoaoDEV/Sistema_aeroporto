# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Autor: Brendon João Campos Neves.
# Data: 10/01/2025.
# Módulo onde seram encapsuladas as funções desse pacote em uma classe para facilitar a importação:

# Importando as funções dos outros módulos:
from front_end.limpar_terminal import limpar_terminal
from front_end.submenu_criar import submenu_criar
from front_end.submenu_atualizar import submenu_atualizar
from front_end.submenu_visualizar import submenu_visualizar
from front_end.submenu_deletar import submenu_deletar


# Criação da classe:
class Menu:
    def __init__(self):
        pass

    def limpar_terminal(self):
        return limpar_terminal

    def submenu_criar(self):
        return submenu_criar

    def submenu_atualizar(self):
        return submenu_atualizar

    def submenu_visualizar(self):
        return submenu_visualizar

    def submenu_deletar(self):
        return submenu_deletar
