#!/usr/bin/python
#Author vikitor566


# Importacao
from Tkinter import *
import tkMessageBox
import Tkinter
import os
import random


#Declaracao de variaveis
#vetores
card=[]
tot=[]

#inteiros
result=0
vr=0

#Dicionario
bancos=dict([('B.Boavista',4231),
              ('WCard Bradesco',4551),
              ('Cl.InternetWorld Unibanco',4011),
              ('Amex',3766),
              ('Bradesco',4290),
              ('American Express',4091),
              ('Itau Mastercard',5390),
              ('Unibanco',3622),
              ('Mastercard',5150),
              ('BB',4001),
              ('MBNA Discover',6013),              
              ])


#Funcoes
def gerar(prefixo):
   r=0
   i=0
   s="abc"
   x=0
   global card
   while i < 4:
      s=repr(prefixo)
      x=int(s[i:i+1],10)
      #print x
      card.insert(i,x)
      i=i+1
   while i < 15:
      r=random.uniform(0,9)
      r=r//1
      card.append(int(r))
      i = i + 1
   return card

def testar(cartao):
   global result
   global card
   global tot
   global vr
   i=0
   x=0
   while(i<15):
      y=cartao[i]
      if(i+1%2==0):
         result=result+y   
      elif(i+1%2!=0 and y*2>9):
         result=result+(y*2-9)
      else:
         result=result+y*2
      i=i+1
   j=0   
   y=result
   while (y%10 != 0):
      j=j+1
      y=y+1
   #print j   
   card.append(j)   
   return cartao

def formato(cartao):
   i=0
   y=''
   card=''
   card=''.join(str(cartao))
   card=card.replace(",","")
   card=card.replace("[","")
   card=card.replace("]","")
   card=card.replace(" ","")
   card=card[0:4]+'-'+card[4:8]+'-'+card[8:12]+'-'+card[12:16]
   return card

def final(prefixo):
   x=formato(testar(gerar(prefixo)))
   return x

def rotina():
   global card
   card=[]
   p=Lista.get(Lista.curselection())
   cod=final(bancos[p])
   Texto.insert(END,cod+'\n')


top = Tk()
top.title('Gerador de cartoes')

var = StringVar()
label = Label( top, textvariable=var)
var.set("Selecione o banco")


Lista = Listbox(top, width=50)
for itens in bancos:
   Lista.insert(END,itens)   

Texto=Text(top,state=NORMAL,height=15,width=50)
Botao = Tkinter.Button(top, text ="Gerar", command=rotina)

label.pack(padx=15,pady=15)
Lista.pack(padx=15,pady=15)
Texto.pack(padx=15,pady=15)
Botao.pack(padx=15,pady=15)
top.mainloop()