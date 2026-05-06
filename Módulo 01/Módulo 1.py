'''

CRUD


SALAO DE BELEZA



'''


print('\n === Sistema de Salao de Beleza === \n')


print('1.Ver Agenda')
print('2.Fazer agendamento')
print('3.Escolher Serviço')
print('4.Cancelar Agendamento')
print('5.Mapa')
print('6.Suporte')
print('0.Sair')



while True:

    escolha_menu = input("\n escolha uma opçao: " )
    if escolha_menu == '1':

        print('Ver agenda...')
        nome_cliente = input('digite o nome do cliente:')
        telefone_cliente = input('digite o telefone do cliente:')

    elif escolha_menu == '0':

        print("Saindo do sistema. Ate logo!")
        break


    else:
        print("Opçao invalida. Por favor, tente novmente.")
