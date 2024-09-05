import tkinter
from tkinter import *
from tkinter import ttk

import datetime
import calendar

from PIL import ImageTk, Image, ImageOps, ImageDraw
import requests
from pytube import YouTube
from tkinter.ttk import Progressbar

#DEFINING COLORS
black = '#444466'
white = '#feffff'
blue = '#6f9fbd'
value = '#38576b'
letter = '#403d3d'

background = '#3b3b3b'

#CREATING THE MAIN WINDOW
janela = Tk()
janela.title('')
janela.geometry('500x300')
janela.configure(bg=background)

#FRAMEE CREATION

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)
frame_principal = Frame(janela, width=500, height=110, bg= background, pady=5, padx=0, relief='flat',)
frame_principal.grid(row=2, column=0, sticky=NW) #sticky - NW define que o frame ficará preso ao canto superior esquerdo da janela
#.grid define a posição do frame na grade da janela

frame_quadros = Frame(janela, width=500, height= 300, bg=background, pady= 5, padx= 0, relief= 'flat',) #flat = frame sem bordas
frame_quadros.grid(row=2, column=0, sticky=NW)

logo = Image.open('images/youtube.png')
logo = logo.resize((50, 50), Image.LANCZOS) # lanczos é um método de redimensionamento que a imasera redimensionada usando um algoritmo para evitar distorções
logo = Image.Tk.PhotoImage(logo)
l_logo = Label(frame_principal, image=logo, compound=LEFT, bg=background, fg='white', font=('Ivy 10 bold'), anchor='nw', relief=FLAT)
l_logo.place(x=5, y=10)

app_nome = Label(frame_principal, text='YouTube Installer w Py', width=32, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 15 bold'), bg=background, fg=black)
app_nome.place(x=65, y=15)