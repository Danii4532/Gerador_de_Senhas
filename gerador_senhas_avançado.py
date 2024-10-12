import tkinter.filedialog
from tkinter import filedialog
import random
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.UTF-8')
    
#adicionar uma lista com as palavras que serao usadas para gerar as senhas, para caso ocorra de haver algum problema com o txt que contem as palavras
lista_palavras = ['Amizade', 'Coragem', 'Paciência', 'Honestidade', 'Bondade', 'Maça', 'Banana', 'Laranja', 'Morango', 'Abacaxi', 'Uva', 'Manga', 'Melancia', 'Pera', 'Kiwi', 'Cadeira', 'Mesa', 'Lápis', 'Caneta', 'Livro', 'Relógio', 'Computador', 'Telefone', 'Garrafa', 'Tesoura', 'Mochila', 'Quadro', 'Teclado', 'Monitor', 'Ventilador', 'Caderno', 'Faca', 'Colher', 'Almofada', 'Janela', 'Ana', 'JoÃ£o', 'Maria', 'Pedro', 'Lucas', 'Sofia', 'Matheus', 'Clara', 'Gabriel', 'Laura', 'Bruno', 'Alice', 'Rafael', 'Helena', 'Tiago', 'Julia', 'Leonardo', 'Isabel', 'Carlos', 'Beatriz']


def Salvar_senha(senha):
    loop1 = True
    while loop1:
        opcao = input('Deseja salvar a senha gerada: \n1 - Sim \n2 - Não\n:')   
        if opcao == '1':
            Salvar(senha)
            loop1 = False
        elif opcao == '2':
            Novamente()
            loop1 = False
        else:
            print('Opção inválida')
    

def Letras_e_numeros(num):
    tamanho = num
    senha = ''
    numeros = [str(i) for i in range(10)]
    dificuldade = input('Escolha um nivel de dificuldade da senha: \n1 - Fácil \n2 - Moderada \n3 - Difícil\n:')
    if dificuldade == '1':         
        escolha = random.choice(lista_palavras)
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
        print(f'Senha gerada: {senha}')
        Salvar_senha(senha)

    elif dificuldade == '2':
        senha = ''
        numeros = [str(i) for i in range(10)]
        pontuacao = ['.', ',', '[', ']', '(', ')', '!', '?', ';', ':', '^', '/', '-', '{', '}', '_', '=', '+', '<', '>','#']
        if int(tamanho) == 1:
            senha+=random.choice(pontuacao)
            exit()
    
        escolha = random.choice(lista_palavras)
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
        print(f'Senha gerada: {senha}')
        Salvar_senha(senha)



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
        Salvar_senha(senha)

            

def Numeros(num):
    senha = ''
    numeros = [i for i in range(10)]
    for cada in range(int(num)):
        escolha = random.choice(numeros)
        senha+=str(escolha)
    
    print(f'Senha gerada: {senha}')
    Salvar_senha(senha)

        
def Novamente():
    loop = True
    while loop:
        continuar = input('Escolha \n1 - Continuar \n2 - Sair\n:')
        if continuar == '1':
            loop = False
            Principal()
        elif continuar == '2':
            print('Programa Finalizado')
            exit()
        else:
            print('Opção Inválida')
        
def Letras(num):
    senha = ''
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    for cada in range(int(num)):
        escolha = random.choice(letras)
        senha+=escolha
    print(f'Senha gerada: {senha}')
    Salvar_senha(senha)


loop = 1

def Salvar(senha):
    #oferecer opções para o usuario salvar a senha, tera opções de salvar primeiro em um txt, e talvez em um xlsx
    #oferecer opções avançadas, onde o usuario pode criar mais de 1 senha de uma vez e rotular elas, ex: senha 1 para facebook, etc
    password = ''
    janela = tkinter.Tk()
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
    loop_senha = True
    print('A senha precisa conter ao menos 4 caracteres')
    while loop_senha:
        tamanho = input('Digite quantos caracteres sua senha terá: ')
        if tamanho < '4' or tamanho == ' ':
            print('Valor inserido inválido')
            print('A senha precisa ter no mínimo 4 caracteres')
            Novamente()

        elif tamanho >= '4' and tamanho.isdigit():
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
            loop = False

        else:
            print('Insira apenas números')
            Novamente()

        

Principal()
