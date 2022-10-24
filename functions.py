#bibliotecas
from __future__ import unicode_literals
import youtube_dl
import requests
from pytube import YouTube
from pytube.cli import on_progress
from time import sleep


#função para download de imagem
def imagem_download():
    try:
        url_imagem = str(input('Cole a URL da imagem -> '))
        nome_imagem = str(input('Insíra o nome da imagem a ser salva: '))
        tipo = str(input('Qual o tipo da imagem (.png / .jpg): ')).lower()
        print('Fazendo o download da imagem.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        r = requests.get(url_imagem)
        with open(f'{nome_imagem}' + f'{tipo}', 'wb') as arquivo:
            arquivo.write(r.content)

        print('SUCESSO!')

    except:
        print('Erro! Download não concluído.')

    sleep(1.7)


#função para o download de video
def video_download():
    try:
        link_video = str(input('Insíra o link do vídeo -> '))
        loading = YouTube(link_video, on_progress_callback=on_progress)
        print('Título: ', loading.title)
        print(f'Fazendo o download do vídeo.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        resolution = loading.streams.get_highest_resolution()
        resolution.download()
        print('SUCESSO')

    except:
        print('Erro! Download não concluído.')

    sleep(1.7)


#função para o download da música
def music_download():
    try:
        link_musica = str(input('Insíra o link da musica -> '))
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'avi',
                'preferredquality': '900'
            }],
            'postprocessor_args': [
                '-ar', '9000000000000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{link_musica}'])
        print('SUCESSO')

    except:
        print('Erro! Download não concluído!')

    sleep(1.7)
