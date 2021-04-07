import mysql.connector
from time import sleep
from funcoes import menu,menu3, menu2, menu4
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
    host="localhost",               #hostname
    user="root",                   # the user who has privilege to the db
    passwd="",               #password for user
    database="dbeletronica"
)
dados = []
resconsulta = []
cursor = banco.cursor()

while True:
    print('\n '* 15)
    menu()
    opc = int(input('DIGITE UMA OPÇÃO VALIDA: '))
    if opc == 1:
        cpf = ''
        cmdCadastro = "INSERT INTO clientes (cpf,nome,telefone,email,cidade,bairro,rua) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        while len(cpf) != 11:
            cpf = str(input("CPF: "))
        nome = str(input("NOME: "))
        telefone = str(input("TELEFONE: "))
        email = str(input("EMAIL: "))
        cidade = str(input("CIDADE: "))
        bairro = str(input("BAIRRO: "))
        rua = str(input("RUA: "))
        dados.append(cpf)
        dados.append(nome)
        dados.append(telefone)
        dados.append(email)
        dados.append(cidade)
        dados.append(bairro)
        dados.append(rua)
        cursor.execute(cmdCadastro, dados)
        with open('dados.txt','a') as backup:
            for v in dados:
                backup.write(str(v)+ '\n')
        print('Cadastro e Backup realizado com sucesso.')
    elif opc == 2:
        while True:
            menu2()
            opcConsulta = int(input('DIGITE UMA OPÇÃO VALIDA: '))
            if opcConsulta == 1:
                osCliente = int(input('NUMERO DA ORDEM DE SERVIÇO: '))
                cmdConsulta = f"SELECT * FROM clientes WHERE os = {osCliente}"
                cursor.execute(cmdConsulta)
                resConsulta = cursor.fetchall()
                for r in resConsulta:
                    print(f'Os: {r[0]}')
                    print(f'CPF: {r[1]}')
                    print(f'Nome: {r[2]}')
                    print(f'Telefone: {r[3]}')
                    print(f'Email: {r[4]}')
                    print(f'Endereço Rua {r[7]}, Bairro{r[6]} em {r[5]}')
                    print(f'Data de Entrada: {r[8]}')
                opcPDF = str(input('\nDESEJA UM ARQUIVO PDF ? [S/N]'))
                if opcPDF in 'Ss':
                    for p in resConsulta:
                        pdfDraw = f"OS: {p[0]}, CPF: {p[1]}, Nome: {p[2]}, Telefone: {p[3]}, Email: {p[4]}, Endereço: {p[7]}, Bairro {p[6]} em {p[5]}, Data de Entrada {p[8]}"
                        pdf = canvas.Canvas(f"OS{p[0]}.pdf")
                        pdf.drawString(10,10, pdfDraw)
                        pdf.save()

            elif opcConsulta == 2:
                cpfCliente = int(input('NUMERO DO CPF: '))
                cmdConsulta = f"SELECT * FROM clientes WHERE cpf = {cpfCliente}"
                cursor.execute(cmdConsulta)
                resConsulta = cursor.fetchall()
                for r in resConsulta:
                    print(f'Os: {r[0]}')
                    print(f'CPF: {r[1]}')
                    print(f'Nome: {r[2]}')
                    print(f'Telefone: {r[3]}')
                    print(f'Email: {r[4]}')
                    print(f'Endereço Rua {r[7]}, Bairro{r[6]} em {r[5]}')
                    print(f'Data de Entrada: {r[8]}')

            elif opcConsulta == 3:
                cmdConsulta = "SELECT * FROM clientes WHERE os > 0"
                cursor.execute(cmdConsulta)
                resConsulta = cursor.fetchall()
                for r in resConsulta:
                    print(f'Os: {r[0]}')
                    print(f'CPF: {r[1]}')
                    print(f'Nome: {r[2]}')
                    print(f'Telefone: {r[3]}')
                    print(f'Email: {r[4]}')
                    print(f'Endereço Rua {r[7]}, Bairro{r[6]} em {r[5]}')
                    print(f'Data de Entrada: {r[8]}')
                    print('-='*30)

            sairOpc = str(input('DESEJA CONTINUAR CONSULTANDO [S/N]: '))
            if sairOpc in 'Nn':
                break
    #ALTERACAO DE DADOS
    elif opc == 3:
        while True:
            menu3()
            opcAlteracao = int(input('DIGITE UMA OPÇÃO VALIDA: '))
            if opcAlteracao == 1:
                print('')
            elif opcAlteracao == 2:
                print('')
            sairOpc = str(input('DESEJA CONTINUAR ALTERANDO [S/N]: '))
            if sairOpc in 'Nn':
                break



    #ELIF DE EXCLUSÃO
    elif opc == 4:
        while True:
            menu4()
            opcExclusao = int(input('DIGITE UMA OPÇÃO VALIDA: '))
            if opcExclusao == 1:
                senhaRcon = int(input('DIGITE A SENHA RCON: '))
                if senhaRcon == 142700:
                    confirmRcon = str(input('APOS EXCLUSÃO, NÂO PODERA SER RECUPERADO OS DADOS TEM CERTEZA DISSO? [S/N]: '))
                    if confirmRcon in 'N':
                        break
                    else:
                        osClienteExclusao = int(input('OS QUE DESEJA REMOVER DO SISTEMA: '))
                        cmdDelete = f"DELETE FROM clientes WHERE os = {osClienteExclusao}"
                        cursor.execute(cmdDelete)
                        banco.commit()
            elif opcExclusao == 2:
                break
    #ELIF FECHA O PROGRAMA
    elif opc == 5:
        print(' FECHANDO SEU SISTEMA.')
        sleep(3)
        break
    #OPCAO INVALIDA
    else:
        print('')