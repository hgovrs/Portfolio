from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
import os
from datetime import datetime
import time
from tkinter import messagebox


#Funcoes
#---------------------------------------------#

#------------------FUNCAO QUE RETORNA UM VALOR DO ITEM SELECIONADO NO COMBOBOX-------------#
def callbackFunc(event):
    try: 
        if ProdutosSelecao.get() == 'Produto_1':
            ValorProduto.set(0.80)
        if ProdutosSelecao.get() == 'Produto_2':
            ValorProduto.set(0.90)

        if ProdutosSelecao2.get() == 'Produto_1':
            ValorProduto2.set(0.80)
        if ProdutosSelecao2.get() == 'Produto_2':
            ValorProduto2.set(0.90)

        if ProdutosSelecao3.get() == 'Produto_1':
            ValorProduto3.set(0.80)
        if ProdutosSelecao3.get() == 'Produto_2':
            ValorProduto3.set(0.90)
        
        if ProdutosSelecao4.get() == 'Produto_1':
            ValorProduto4.set(0.80)
        if ProdutosSelecao4.get() == 'Produto_2':
            ValorProduto4.set(0.90)

        if ProdutosSelecao5.get() == 'Produto_1':
            ValorProduto5.set(0.80)
        if ProdutosSelecao5.get() == 'Produto_2':
            ValorProduto5.set(0.90)

        if ProdutosSelecao6.get() == 'Produto_1':
            ValorProduto6.set(0.80)
        if ProdutosSelecao6.get() == 'Produto_2':
            ValorProduto6.set(0.90)

        if ProdutosSelecao7.get() == 'Produto_1':
            ValorProduto7.set(0.80)
        if ProdutosSelecao7.get() == 'Produto_2':
            ValorProduto7.set(0.90)

        if ProdutosSelecao8.get() == 'Produto_1':
            ValorProduto8.set(0.80)
        if ProdutosSelecao8.get() == 'Produto_2':
            ValorProduto8.set(0.90)
        
    except ValueError:
        print('error')


# -------------------------- FUNCAO PARA ALTERAR TEMA DO APP ------------------#
def callbackFunc2(eventObject):      
        
    if temasCombo.get() == 'Rose':
        style.set_theme('clearlooks')
        style.configure('.', foreground='gray26', background ='pink')
        my_label.configure(image = rosa)
        notaL1.configure(background ='floral white')
        notaL2.configure(background ='floral white')
        notaL3.configure(background ='floral white')
        notaL4.configure(background ='floral white')
        notaL5.configure(background ='floral white')
        colunn0.grid(row=0, column=0, pady =12, padx=26)
        agctaEntry.place(x = 200, y = 418)
        
    if temasCombo.get() == 'Dados':
        style.set_theme('elegance')
        style.configure('.', foreground='black', background ='#cdcdcd')
        my_label.configure(image = elegance)
        colunn0.grid(row=0, column=0, pady =12, padx=23)
        agctaEntry.place(x = 200, y = 418)


#---------------------------------------FUNCAO SOMA----------------------------------------*   
 
#------------------------FUNCAO SOMA, SOMA TODOS OS PONTOS DOS PRODUTOS   #      
def soma():
    
    try:
        n1 = float(ValorProduto.get())
        n2 = int(QuantidadeProduto.get())
        r = n1 * n2
        v.set('%.2f'%(r))

        n3 = float(ValorProduto2.get())
        n4 = int(QuantidadeProduto2.get())   
        r2 = n3 * n4
        v2.set('%.2f'%(r2))

        n5 = float(ValorProduto3.get())
        n6 = int(QuantidadeProduto3.get())   
        r3 = n5 * n6
        v3.set('%.2f'%(r3))  

        n7 = float(ValorProduto4.get())
        n8 = int(QuantidadeProduto4.get())   
        r4 = n7 * n8
        v4.set('%.2f'%(r4))

        n9 = float(ValorProduto5.get())
        n10 = int(QuantidadeProduto5.get())   
        r5 = n9 * n10
        v5.set('%.2f'%(r5))

        n11 = float(ValorProduto6.get())
        n12 = int(QuantidadeProduto6.get())   
        r6 = n11 * n12
        v6.set('%.2f'%(r6))

        n13 = float(ValorProduto7.get())
        n14 = int(QuantidadeProduto7.get())   
        r7 = n13 * n14
        v7.set('%.2f'%(r7))

        n15 = float(ValorProduto8.get())
        n16 = int(QuantidadeProduto8.get())   
        r8 = n15 * n16
        v8.set('%.2f'%(r8))

    finally:
        totalPontos =  r + r2 + r3 + r4 + r5 + r6 + r7 + r8
        totalpontos.set('%.2f'%(totalPontos))

        nota = totalPontos
        if nota > 45:
            notaL5.configure(borderwidth=1, relief='solid', background ='salmon')
          
        elif nota >= 37:
            notaL4.configure(borderwidth=1, relief='solid', background ='lime green')
             
        elif nota >= 31:
            notaL3.configure(borderwidth=1, relief='solid', background ='forestgreen')
            
        elif nota >= 26:
            notaL2.configure(borderwidth=1, relief='solid', background ='goldenrod')
             
        elif nota < 26:
            notaL1.configure(borderwidth=1, relief='sunken', background ='indian red')
            
    
    var_barra.set(totalPontos)

#-----------------------FUNCAO PARA SALVAR PRODUCAO EM ARQUIVO TXT -----------------------#

def salvar_producao(): 
    lines = open('./Producao Detalhada/user.txt').read().splitlines()
    lines[4] = 'Produto: '+ ProdutosSelecao.get()+' Ponderador: ' +ValorProduto.get()+' Quantidade: '+QuantidadeProduto.get()+' Total De Pontos Produto: '+v.get()
    lines[6] = 'Produto: '+ ProdutosSelecao2.get()+' Ponderador: ' +ValorProduto2.get()+' Quantidade: '+QuantidadeProduto2.get()+' Total De Pontos Produto: '+v2.get()
    lines[8] = 'Produto: '+ ProdutosSelecao3.get()+' Ponderador: ' +ValorProduto3.get()+' Quantidade: '+QuantidadeProduto3.get()+' Total De Pontos Produto: '+v3.get()
    lines[10] = 'Produto: '+ ProdutosSelecao4.get()+' Ponderador: ' +ValorProduto4.get()+' Quantidade: '+QuantidadeProduto4.get()+' Total De Pontos Produto: '+v4.get()
    lines[12] = 'Produto: '+ ProdutosSelecao5.get()+' Ponderador: ' +ValorProduto5.get()+' Quantidade: '+QuantidadeProduto5.get()+' Total De Pontos Produto: '+v5.get()
    lines[14] = 'Produto: '+ ProdutosSelecao6.get()+' Ponderador: ' +ValorProduto6.get()+' Quantidade: '+QuantidadeProduto6.get()+' Total De Pontos Produto: '+v6.get()
    lines[16] = 'Produto: '+ ProdutosSelecao7.get()+' Ponderador: ' +ValorProduto7.get()+' Quantidade: '+QuantidadeProduto7.get()+' Total De Pontos Produto: '+v7.get()
    lines[18] = 'Produto: '+ ProdutosSelecao8.get()+' Ponderador: ' +ValorProduto8.get()+' Quantidade: '+QuantidadeProduto8.get()+' Total De Pontos Produto: '+v8.get()
    lines[20] = 'Total de Pontos no Dia: '+ totalpontos.get()
   
    open('./Producao Detalhada/user.txt','w').write('\n'.join(lines))
                                         #faz a substituiçao das linhas dos arquivos
                                                                        #entao sempre q apertar salvar producao, vai salvar nas mesmas linhas


#-------------------------------FUNCAO PARA ADICIONAR AG E CONTA NO MESMO ARQUIVO TXT DE SALVAR PRODUCAO--------------------#

def agecta():
    file = open('./Producao Detalhada/user.txt', 'r') #abro o arquivo modo leitura
    addagcEcta = file.readlines() #leio todas as linhas
    addagcEcta.append('AG e Conta: '+agctaEntry.get()+ '\n ') #adiciono linhas no final da leitura
    file = open('./Producao Detalhada/user.txt', 'w') #abro o arquivo como edicao
    file.writelines(addagcEcta)#escrevo a variavendo em parentes
    file.close()
    agctaEntry.delete (0, END)
    agctaEntry.insert (0, "ag e cta" )
    print('feito')



#--------------------------Quando fechar o aplicativo ativa essa funcao de renomear o arquivo-------------------------------*

def gravarRenomear():
    try:
        
        if messagebox.askyesno('Minha Produção 1.0', 'Deseja Sair e Salva Produção?') == True:
            totalP = soma()
            totalP
            salvar = salvar_producao()
            salvar
            
            
            os.rename('./Producao Detalhada/user.txt', './Producao Detalhada/'+time.strftime("Data_%d-%m-%Y-Hora_%H_%M_%S.txt"))
            
       
            app.destroy()
        else:
            print('ok')

    except:
        file = open('./Producao Detalhada/user.txt', 'w')
        file.close()
        os.rename('./Producao Detalhada/user.txt', './Producao Detalhada/'+time.strftime("Data_%d-%m-%Y-Hora_%H_%M.txt"))
        app.destroy()
        

        




#APP TKINTER
#------------------------------------------------------------------------#
app = tk.Tk() 
app.geometry('430x500+560+290') 
app.title('Minha Produção 1.0')
app.resizable(False, False) 
app.iconbitmap('./img/icon2.ico')
style = ThemedStyle(app)
style.set_theme('scidblue')
style.configure('.', foreground='gray26', background ='linen')
app.protocol('WM_DELETE_WINDOW', gravarRenomear)  # root is your root window



#--- Criar pasta nova
pasta_nova = './Producao Detalhada'
try:
    os.mkdir(pasta_nova)
except FileExistsError as e:
    pass

try:
    file = open('./Producao Detalhada/user.txt', 'w')
    file.write('--------------------------------- Producao log ---------------------------------------\n \n')
    file.write('Produção Realizada no Dia :\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n')
    file.write('--------------------------------- Contas atuadas no dia : ---------------------------------------\n \n')
    file.close()
except FileExistsError as e:
    pass

#---------- uma linha e uma coluna pra centralizar o conteudo ------------#
colunn0= ttk.Label(app)
colunn0.grid(row=0, column=0, pady =12, padx=26)

#------------ Imagem de fundo ---------------------------------#
my_img = ImageTk.PhotoImage(file="./img/dark2.png")
my_label = ttk.Label(image=my_img)
my_label.place(x=0 , y=0)
rosa = ImageTk.PhotoImage(file="./img/rosa.png")
elegance = ImageTk.PhotoImage(file="./img/elegance.png")



# ---------------------- Adicionar agencia e conta no arquivo txt --------------------#
agctaEntry = ttk.Entry(app, width = 12)
agctaEntry.place(x = 200, y = 415)
agctaEntry.insert (0, "ag e cta" )


bttagCta = ttk.Button(app, text ='+', width = 0.2, command= agecta)
bttagCta.place(x = 280, y = 415)


#------------- Botao salvar producao em arquivo Txt ------------------- #

gravarProducao = ttk.Button(app, text ='Salvar Produção', width=14, command = salvar_producao)
gravarProducao.place(x = 51, y = 455)

#-----------------------BOTAO MOSTRAR TOTAL DE PONTOS REALIZADOS ----------------------------------------------------------------#
BotaoMostrarPontos = ttk.Button(app, text ='Ver Pontos',width=14, command = soma)
BotaoMostrarPontos.place(x = 51, y = 415)

# ------------------------MOSTRAR A NOTA ----------------------------------------------------*




#---------------------------SELECIONAR TEMAS DIFERENTE PARA O PROGRAMA ---------------------------------------*
temas = ['Rose', 'Dados']

temasCombo = ttk.Combobox(app, values=temas, width=6, font='Arial 9')
temasCombo.place(x = 200, y = 455)
temasCombo.bind("<<ComboboxSelected>>", callbackFunc2)
temasCombo.set('Temas')


#----------------------------BARRA DE PROGRESSO  ---------------------------#
var_barra = DoubleVar()
minha_barra = ttk.Progressbar(app, variable=var_barra, maximum=49).place(x =1, y = 370, width=429, height=20)
var_barra.set(1)


#------------------------Produtos Inseridos no COMBOBOX ------------------------------------#
lista = ['Produto_1', 'Produto_2', 'Produto_3', 'Produto_4', 'Produto_5', 'Produto_6', 'Produto_7', 'Produto_8',
        'Produto_9', 'Produto_10']

totalpontos = StringVar()
tk.Label(app, textvariable= totalpontos, background='linen').place(x = 200, y = 326)
totalpontos.set('')

#------------------- COLUNAS DE NOTAS ---------------#

notaL1 = ttk.Label(app, width= 38, text = 'N1', background ='tan1', borderwidth=1, relief='groove')
notaL1.place(x = 1, y = 349)
notaL1.config(anchor=CENTER)
notaL2 = ttk.Label(app, width= 10  , text = 'N2', background ='tan1', borderwidth=1, relief='groove' )
notaL2.place(x = 228, y = 349)
notaL3 = ttk.Label(app, width= 10, text = 'N3', background ='tan1', borderwidth=1,  relief='groove')
notaL3.place(x = 275, y = 349)
notaL4 = ttk.Label(app, width= 12 , text = 'N4', background ='tan1',borderwidth=1,  relief='groove' )
notaL4.config(anchor=CENTER)
notaL4.place(x = 326, y = 349)
notaL5 = ttk.Label(app, width= 6 , text = 'N5', background ='tan1', borderwidth=1,  relief='groove')
notaL5.place(x = 395, y = 349)
notaL5.config(anchor=CENTER)


#----- SELECAO DE PRODUTOS + VALOR DO PRODUTO + QUANTIDADEPRODUTO + PONTOS REALIZADOS PRODUTO-----------------------------------------*
ValorProduto = StringVar()
ttk.Entry(app, textvariable = ValorProduto, width=4, font='Arial 14').grid(column = 2, row=  1)
ValorProduto.set(0)



QuantidadeProduto = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 1)
QuantidadeProduto.set(0)


v = StringVar()
ttk.Label(app, textvariable= v, width=5, font='Arial 13').grid(column=4, row=1)
v.set('')

ProdutosSelecao = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao.grid(column=1, row=1)
ProdutosSelecao.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 2 + VALOR DO PRODUTO 2+ QUANTIDADEPRODUTO 2 + PONTOS REALIZADOS PRODUTO-2----------------------------------------*

ValorProduto2 = StringVar()
ttk.Entry(app, textvariable = ValorProduto2, width=4, font='Arial 14').grid(column = 2, row= 2)
ValorProduto2.set(0)

QuantidadeProduto2 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto2, from_=0, to = 100, width=3, font='Arial 14').grid(column=3, row=2)
QuantidadeProduto2.set(0)

v2 = StringVar()
ttk.Label(app, textvariable= v2, width=5, font='Arial 13').grid(column=4, row=2)
v2.set('')

ProdutosSelecao2 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao2.grid(column=1, row=2)
ProdutosSelecao2.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao2.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 3 + VALOR DO PRODUTO3 + QUANTIDADEPRODUTO3 + PONTOS REALIZADOS PRODUTO3-----------------------------------------*
ValorProduto3 = StringVar()
ttk.Entry(app, textvariable = ValorProduto3, width=4, font='Arial 14').grid(column = 2, row= 3)
ValorProduto3.set(0)

QuantidadeProduto3 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto3, from_=0, to = 100, width=3, font='Arial 14').grid(column=3, row=3)
QuantidadeProduto3.set(0)

v3 = StringVar()
ttk.Label(app, textvariable= v3, width=5, font='Arial 13').grid(column=4, row=3)
v3.set('')

ProdutosSelecao3 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao3.grid(column=1, row=3)
ProdutosSelecao3.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao3.set('Selecionar Produto')


#----- SELECAO DE PRODUTOS 4 + VALOR DO PRODUTO 4 + QUANTIDADEPRODUTO  4+ PONTOS REALIZADOS PRODUTO 4-----------------------------------------*
ValorProduto4 = StringVar()
ttk.Entry(app, textvariable = ValorProduto4, width=4, font='Arial 14').grid(column = 2, row=  4)
ValorProduto4.set(0)


QuantidadeProduto4 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto4, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 4)
QuantidadeProduto4.set(0)

v4 = StringVar()
ttk.Label(app, textvariable= v4, width=5, font='Arial 13').grid(column=4, row=4)
v4.set('')

ProdutosSelecao4 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao4.grid(column=1, row=4)
ProdutosSelecao4.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao4.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 5 + VALOR DO PRODUTO 5+ QUANTIDADEPRODUTO 5+ PONTOS REALIZADOS PRODUTO 5-----------------------------------------*
ValorProduto5 = StringVar()
ttk.Entry(app, textvariable = ValorProduto5, width=4, font='Arial 14').grid(column = 2, row=  5)
ValorProduto5.set(0)


QuantidadeProduto5 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto5, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 5)
QuantidadeProduto5.set(0)

v5 = StringVar()
ttk.Label(app, textvariable= v5, width=5, font='Arial 13').grid(column=4, row=5)
v5.set('')

ProdutosSelecao5 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao5.grid(column=1, row=5)
ProdutosSelecao5.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao5.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 6+ VALOR DO PRODUTO 6+ QUANTIDADEPRODUTO 6+ PONTOS REALIZADOS PRODUTO 6-----------------------------------------*
ValorProduto6 = StringVar()
ttk.Entry(app, textvariable = ValorProduto6, width=4, font='Arial 14').grid(column = 2, row=  6)
ValorProduto6.set(0)


QuantidadeProduto6 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto6, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 6)
QuantidadeProduto6.set(0)

v6 = StringVar()
ttk.Label(app, textvariable= v6, width=5, font='Arial 13').grid(column=4, row=6)
v6.set('')

ProdutosSelecao6 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao6.grid(column=1, row=6)
ProdutosSelecao6.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao6.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 7+ VALOR DO PRODUTO 7+ QUANTIDADEPRODUTO 7+ PONTOS REALIZADOS PRODUTO 7-----------------------------------------*
ValorProduto7 = StringVar()
ttk.Entry(app, textvariable = ValorProduto7, width=4, font='Arial 14').grid(column = 2, row=  7)
ValorProduto7.set(0)


QuantidadeProduto7 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto7, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 7)
QuantidadeProduto7.set(0)

v7 = StringVar()
ttk.Label(app, textvariable= v7, width=5, font='Arial 13').grid(column=4, row=7)
v7.set('')

ProdutosSelecao7 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao7.grid(column=1, row=7)
ProdutosSelecao7.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao7.set('Selecionar Produto')

#----- SELECAO DE PRODUTOS 8+ VALOR DO PRODUTO 8+ QUANTIDADEPRODUTO 8+ PONTOS REALIZADOS PRODUTO 8-----------------------------------------*

ValorProduto8 = StringVar()
ttk.Entry(app, textvariable = ValorProduto8, width=4, font='Arial 14').grid(column = 2, row=  8)
ValorProduto8.set(0)


QuantidadeProduto8 = StringVar()
ttk.Spinbox(app, textvariable = QuantidadeProduto8, from_=0, to = 100, width=3, font='Arial 14').grid(column= 3, row= 8)
QuantidadeProduto8.set(0)

v8 = StringVar()
ttk.Label(app, textvariable= v8, width=5, font='Arial 13').grid(column=4, row=8)
v8.set('')

ProdutosSelecao8 = ttk.Combobox(app, values=lista, width=15, font='Arial 14')
ProdutosSelecao8.grid(column=1, row=8)
ProdutosSelecao8.bind("<<ComboboxSelected>>", callbackFunc)
ProdutosSelecao8.set('Selecionar Produto')



app.mainloop()