list=[]
while True:
    print('----------FAZENTECH----------\n')
    print(' [1] CADASTRO DE FUNCIONARIOS \n [2] CADASTRO PRODUÇÃO DE LEITE \n [3] CADASTRO DE PRODUTO \n [4] CADASTRO VAREJISTAS \n')
    x=int(input('ESCOLHE UMA OPÇÃO: '))
    while x == 1:
        print('-'*100)
        print(' NOVO CADASTRO DE FUNCIONARIOS ')
        print('-'*100)
        nome= input('NOME: ')
        salario = float(input('SALARIO: R$'))
        função = input('FUNÇÃO:')
        equipamento=input('EQUIPAMENTO: ')
        print('-'*100)
        print('\n NOME: {} \n SALARIO: R${:3.2f} \n FUNÇÃO: {} \n EQUIPAMENTO: {}\n'.format(nome,salario, função,equipamento).upper())
        print('-' * 100)
        x=str(input('\n DESEJA CONTINUAR S/N? \n ').upper())
        if x == 'N':
            print('================EXIT=================')
            exit()
        while x == 'S':
            print('\n')
            break
    while x == 2:
        print('-'*100)
        print(' CADASTRO PRODUÇÃO DE LEITE ')
        print('-'*100)
        id= input('IDENTIFICAÇÃO DA VACA: ')
        colheita = input('DATA DA COLHEITA: ')
        temperatura = input('TEMPERATURA DO LEITE: ')
        produrividade = input('PRODUTIVIDADE: ')
        print('\n IDENTIFICAÇÃO: {} \n COLHEITA: {} \n TEMPERATURA: DO LEITE: {} \n PRODUTIVIDADE: {} \n '.format(id,colheita,temperatura,produrividade))
        x = str(input('\n DESEJA CONTINUAR S/N? \n ').upper())
        if x == 'N':
            print('===============EXIT================')
            exit()
        while x == 'S':
            print('\n')
            break
    while x == 3:
        print('-'*100)
        print(' CADASTRO PRODUTO ')
        print('-'*100)
        preço = input('PREÇO: ')
        estoque = input('ESTOQUE: ')
        print('\n PREÇO: {} \n ESTOQUE: {} \n '.format(preço,estoque,))
        x = str(input('\n DESEJA CONTINUAR S/N? \n ').upper())
        if x == 'N':
            print('===============EXIT================')
            exit()
        while x == 'S':
            print('\n')
            break
    while x == 4:
        print('-'*100)
        print(' CADASTRO DE VAREJISTA ')
        print('-'*100)
        nome = input('NOME: ')
        fantasia = input('NOME FANTASIA: ')
        cep = input('CEP: ')
        numero=input('N°: ')
        cnpj = input('CNPJ: ')
        telefone = input('TELEFONE: ')
        email= input('EMAIL: ')
        print('\n NOME: {} \n NOME FANTASIA: {} \n CEP: {} \n CNPJ: {} \n TELEFONE: {} \n EMAIL: {} '.format(nome, fantasia,cep, cnpj, telefone, email))
        x = str(input('\n DESEJA CONTINUAR S/N? \n ').upper())
        if x == 'N':
            print('===============EXIT================')
            exit()
        while x == 'S':
            print('\n')
            break
