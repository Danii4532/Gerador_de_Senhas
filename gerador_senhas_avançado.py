import tkinter.filedialog
from tkinter import filedialog
import random
#dando ao usuario opções para criar a senha


def Letras_e_numeros(num):
    tamanho = num
    senha = ''
    numeros = [str(i) for i in range(10)]
    dificuldade = input('Escolha um nivel de dificuldade da senha: \n1 - Fácil \n2 - Moderada \n3 - Difícil')
    if dificuldade == '1':
        with open('database.txt', 'r') as arquivo:
            palavras = [palavra for palavra in arquivo]
            escolha = random.choice(palavras)
            tamanho = int(tamanho)
            senha+=escolha[0:int(tamanho)-1]
            senha+=random.choice(numeros)
        if senha == tamanho:
            pass
        elif len(senha) < tamanho:
            x = int(tamanho)-len(senha)+1
            for c in range(x):
                senha+=random.choice(numeros)
        elif len(senha) > tamanho:
            pass
        else:
            pass
        print('Senha gerada: ',senha)
        print('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não')
        opcao = input('\n:')
        if opcao == '1':
            Salvar(senha)
        elif opcao == '2':
            Novamente()

    elif dificuldade == '2':
        senha = ''
        numeros = [str(i) for i in range(10)]
        pontuacao = ['.', ',', '[', ']', '(', ')', '!', '?', ';', ':', '^', '/', '-', '{', '}', '_', '=', '+', '<', '>','#']
        if int(tamanho) == 1:
            senha+=random.choice(pontuacao)
            exit()
        with open('database.txt', 'r') as arquivo:
            palavras = [palavra for palavra in arquivo]
            escolha = random.choice(palavras)
            tamanho = int(tamanho)
            senha+=random.choice(pontuacao)
            senha+=escolha[0:int(tamanho)-3]
            senha+=random.choice(numeros)
            senha+=random.choice(pontuacao)
        if senha == tamanho:
            print('preenchido')
        elif len(senha) < tamanho:
            x = int(tamanho)-len(senha)+1
            for c in range(x):
                senha+=random.choice(numeros)
        elif len(senha) > tamanho:
            pass

        else:
            pass
        print(senha)
        print('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não')
        opcao = input('\n:')
        if opcao == '1':
            Salvar(senha)
        elif opcao == '2':
            Novamente()


    elif dificuldade == '3':
        valor = tamanho
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numeros = [str(i) for i in range(10)]
        senha = ''
        for cada in range(int(valor)):
            if cada%2==0:
                escolha1 = random.choice(letras)
                senha += escolha1
            else:
                escolha2 = random.choice(numeros)
                senha+=escolha2
        print(f'Senha gerada: {senha}')
        print('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não')
        opcao = input('\n:')
        if opcao == '1':
            Salvar(senha)
        elif opcao == '2':
            Novamente()

def Numeros(num):
    senha = ''
    numeros = [i for i in range(10)]
    for cada in range(int(num)):
        escolha = random.choice(numeros)
        senha+=str(escolha)
    print(senha)
    print(f'Senha gerada: {senha}')
    print('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não')
    opcao = input('\n:')
    if opcao == '1':
        Salvar(senha)
    elif opcao == '2':
        Novamente()
def Novamente():

    continuar = input('Escolha \n1 - Continuar \n2 - Sair')
    if continuar == '1':
        loop = 1
    else:
        print('Programa Finalizado')
        exit()
def Letras(num):
    senha = ''
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    for cada in range(int(num)):
        escolha = random.choice(letras)
        senha+=escolha
    print(f'Senha gerada: {senha}')
    print('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não')
    opcao = input('\n:')
    if opcao == '1':
        Salvar(senha)
    elif opcao == '2':
        Novamente()

loop = 1

def Salvar(senha):
    #oferecer opções para o usuario salvar a senha, tera opção de salvar em um txt
    password = ''
    janela = tkinter.Tk()
    janela.withdraw()
    diretorio = filedialog.askdirectory()
    caminho = diretorio+'/Senha_gerada.txt'
    print(caminho)
    password = senha
    print('Deseja adicionar titulo a senha, pode ajudar a se lembrar em qual programa você usará ela \n1 - Sim \n2 - Não')
    op = input(': ')
    if op == '1':
        titulo = input('Digite o titulo que deseja colocar: ')
        with open(caminho,'a') as arquivo:
            arquivo.write(titulo+':')
            arquivo.write(password)
            arquivo.write('\n')
            print("Arquivo 'Senha_gerada.txt' salvo com sucesso em:", caminho)
            Novamente()
    elif op == '2':
        Novamente()

    print('Senhas salvas')

def Principal():
    while loop:
        tamanho = input('Digite quantos caracteres sua senha terá: ')
        if tamanho.isdigit():
            pass

        elif tamanho == ' ':
            print('Insira apenas números')
            Novamente()

        else:
            print('Insira apenas números')
            Novamente()

        print('''
        Escolha uma opção de senha
        1 - Letras e numeros
        2 - Apenas de números
        3 - Apenas letras
        ''')
        op = input(': ')
        if op == '1':
            Letras_e_numeros(tamanho)

        elif op == '2':
            Numeros(tamanho)

        elif op == '3':
            Letras(tamanho)

        else:
            print('Opção Inválida, insira apenas os números disponíveis')
            Novamente()

Principal()
