import os

def processar_respostas(resposta,nome):
    if resposta == "1":
        print(f'{os.linesep}{nome}Olá{os.linesep}')
    elif resposta == "2":
        print(f'{os.linesep}{nome}Tudo{os.linesep}')
    elif resposta == "3":
        print(f'{os.linesep}{nome}Bem{os.linesep}')
    else:
        print('Digite 1,2 ou 3')
    
    

def start():
    print('Olá, bem vindo a central de problemas')
    nome = input('Digite o seu nome: ')
    email = input('Digite seu e-mail: ')
    resposta = input(f'O que gostaria de saber hoje? {os.linesep}[1] - Devoluções{os.linesep}[2] - Reclamações{os.linesep}[3] - Duvidas sobre diluições de produtos Renko{os.linesep}\nDigite o número correspondente a dúvida - ')
    processar_respostas(resposta, nome)
if __name__ == "__main__":
    start()