import random

print("Bem vindo ao gerador de senhas!")

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?+-/,0123456789'

qtdSenhas = int(input("Quantas senhas deseja gerar? "))
tamanhoSenhas = int(input("Qual o tamanho da senha que você deseja? "))

for senhas in range(qtdSenhas):
    senha = ''
    for tamanho in range(tamanhoSenhas):
        senha += random.choice(caracteres)
    print(senha)

