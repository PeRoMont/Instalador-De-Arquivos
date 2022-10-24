#biblioteca
import functions

while True:
    print('====' * 9)
    option = int(input('\t   Download de Arquivos'
          '\nOpções disponíveis:'
                       '\n[0] - Sair do programa'
                       '\n[1] - Baixar imagem da WEB'
                       '\n[2] - Baixar arquivo Mp4'
                       '\n[3] - Baixar arquivo Mp3'
                       '\nInsira a opção desejada: '))
    print('====' * 9)

    while option < 0 or option > 3:
        option = int(input('OPÇÃO INVÁLIDA! Escolha uma das opções disponíveis: '))

    if option == 1:
        functions.imagem_download()

    elif option == 2:
        functions.video_download()

    elif option == 3:
        functions.music_download()
        break

    elif option == 0:
        break

print('***' * 10)
print('\tPrograma finalizado!\n\t Muito obrigado :-D')
print('***' * 10)
