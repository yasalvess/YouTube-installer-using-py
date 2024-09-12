import tkinter
from tkinter import *
from tkinter import ttk

import datetime
import calendar

from PIL import ImageTk, Image, ImageOps, ImageDraw
import requests
from pytube import YouTube
import yt_dlp
from tkinter.ttk import Progressbar

#DEFINING COLORS
black = '#444466'
white = '#feffff'
blue = '#6f9fbd'
value = '#38576b'
letter = '#feffff'

background = '#3b3b3b'

#CREATING THE MAIN WINDOW
janela = Tk()
janela.title('')
janela.geometry('500x300')
janela.configure(bg=background)

#FRAMEE CREATION

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)

frame_principal = Frame(janela, width=500, height=110, bg= background, pady=5, padx=0, relief='flat',)
frame_principal.grid(row=1, column=0) 
#.grid define a posição do frame na grade da janela

frame_quadros = Frame(janela, width=500, height= 300, bg=background, pady= 12, padx= 0, relief= 'flat',) #flat = frame sem bordas
frame_quadros.grid(row=2, column=0, sticky=NW) #sticky - NW define que o frame ficará preso ao canto superior esquerdo da janela

logo = Image.open('images/youtube.png')
logo = logo.resize((50, 50), Image.LANCZOS) # lanczos é um método de redimensionamento que a imasera redimensionada usando um algoritmo para evitar distorções
logo = ImageTk.PhotoImage(logo)
l_logo = Label(frame_principal, image=logo, compound=LEFT, bg=background, fg='white', font=('Ivy 10 bold'), anchor='nw', relief=FLAT)
l_logo.place(x=5, y=10)

app_nome = Label(frame_principal, text='YouTube Installer w Py', width=32, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 15 bold'), bg=background, fg=white)
app_nome.place(x=65, y=15)

def search():
    global img
    url = e_url.get() #obtem o texto do campo de entrada e armazena
    yt = YouTube(url) #cria um objeto com a url do video
    
    #title of video
    title = yt.title
    #numer of views of video
    view = yt.views
    
    #lenght of video
    duration = str(datetime.timedelta(seconds=yt.length)) # obtem a duração do video e converte pra uma string 'HH:MM;SS'
    
    #cover of the video
    cover = yt.thumbnail_url
    
    print(cover)                                                                                                                                                                                                                                                                                            
    
    img_ = Image.open(requests.get(cover, stream=True).raw) #abre a imagem da capa do video
    img_ = img_.resize((230, 150), Image.LANCZOS) #converte a imagem para um formato compativel com o Tkinter
    img_ = ImageTk.PhotoImage(img_) #armazena a imagem redimensionada na variavel 'img'
    
    img = img_
    l_image['image'] = img
    
    #define o titulo com o valor da variavel title
    l_title['text'] = 'Título : '+ str(title)
    #define o texto da visualização 
    l_view['text'] = 'Views : ' + str('{:,}'.format(view))
    #define o texto da duração
    l_time['text'] = 'Duracao : ' + str(duration) 

previousprogress = 0

#função que será chamada durante o download
def on_progress(stream, chunck, bytes_remaining):
    #acessa a variável global
    global previousprogress
    #calcula o tamanho total do arquivo
    total_size = stream.file_size()
    #calcula o número de bytes baixados
    bytes_downloaded = total_size - bytes_remaining
    
    #calcula o progresso em porcentagem
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    #verifica se o progresso atual é maior que o anterior
    if liveprogress > previousprogress:
        #atualiza o valor da variavel previousprogress
        previousprogress = liveprogress
        #imprime o progresso atual
        print(liveprogress)
        #posiciona a barra de progresso na janela
        bar.place(x=250, y=120)
        #atualiza o valor da barra de progresso
        bar['value'] = liveprogress
        #atualiza a janela para receber mudanças
        janela.update_idletasks()

#função que inicia o download do video
def download():
    url = e_url.get()
      # Definindo opções de download
    ydl_opts = {
        'format': 'best',  # Baixa o melhor formato disponível
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Caminho de saída
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Download concluído!")
		    

#cria um label pra exibir o texto
l_url = Label(frame_principal, text='Insira a URL', height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=background, fg=white)
l_url.place(x=10, y=80)

e_url = Entry(frame_principal,width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80)

b_search = Button(frame_principal, text='Search', width=10, height=1, bg=blue, fg=white, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE, command= lambda:search())
b_search.place(x=404, y=80)

# OPERATIONS

#CRIANDO LABEL P/ EXIBIR A IMAGEM
l_image = Label(frame_quadros, compound=LEFT, bg=background, fg=white, font=('Ivy 10 bold'), anchor='nw', relief=FLAT)
l_image.place(x=10, y=10)

l_title = Label(frame_quadros, height=2, pady=0, padx=0, relief='flat', wraplength=225, compound=LEFT, justify='left', anchor=NW, font=('Ivy 10 bold'), bg=background, fg=white)
l_title.place(x=250, y=15)

l_view = Label(frame_quadros, height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=background, fg=white)
l_view.place(x=250, y=40)

l_time = Label(frame_quadros, height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=background, fg=white)
l_time.place(x=250, y=65)

#abre a imagem do botao de download
down = Image.open('images/icon-download.png')
down = down.resize((40, 40))
down = ImageTk.PhotoImage(down)

b_download = Button(frame_quadros, image=down, bg=background, fg=white, font=('Ivy 10 bold'), relief=FLAT, overrelief=RIDGE, command=download)
b_download.place(x=444, y=85)

#cria um obj style p/ configurar o estilo dos widgets
style = ttk.Style()
#define um tema padrão para os widgets
style.theme_use('default')
#configura o estilo da barra de progresso horizontal
style.configure('black.Horizontal.TProgressbar', background='#00E676')
#configura a espessura da barra de progresso
style.configure('TProgressbar', thickness=6)

#cria barra de progresso
bar = Progressbar(frame_quadros, length=190, style='black.Horizontal.TProgressbar')

janela.mainloop()