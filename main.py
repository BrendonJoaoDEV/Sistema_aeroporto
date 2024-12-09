# Curso de Desenvolvimento de Sistemas.
# Turma 0152.
# Professor: Brendon João Campos Neves.
# Data: 09/12/2024 - 
# Módulo main resoponsável pela junção e uso dos demais módulos,
# Além também da lógica principal de funcionamento do sistema.

# Importação das bibliotecas e módulos que serão usados:
import os
import time
from prettytable import PrettyTable
from crud.classe_sistema import Sistema
from banco_dados.criacao_tabelas import criar_banco

# Chamada da função pra criar o banco:
criar_banco()

# Criar um operador do sistema:
operador = Sistema()

# Início do ciclo principal do sistema:
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('<:=:=:=:> MENU <:=:=:=:>')
    print('0 - Sair')
    print('1 - Criar registro')
    print('2 - Ler registro')
    print('3 - Atualizar registro')
    print('4 - Deletar registro')
    
    opcao = input('Digite o númeroda opção que deseja: ').strip()
    
    if opcao == '0':
        print('Saindo do sistema...')
        time.sleep(1)
        break
    
    elif opcao == '1':
        pass
    elif opcao == '2':
        pass
        # Campos, tabelas e condicao
    elif opcao == '3':
        pass
        # tabela, identificador, novo_registro
    elif opcao == '4':
        pass
        # Tabela e identificador
    else:
        pass
    break