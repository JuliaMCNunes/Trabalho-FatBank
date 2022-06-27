from cgi import test
from cgitb import text
from itertools import count
from re import I, L
import tkinter
from tkinter import *
from random import *
from tkinter import ttk
import time
import os
import tkinter.messagebox
#import posiciona
from Classe_Cliente import *
from Classe_Conta import *
from Classe_Historico import *

raf = '8525'
senhaf = '9632'

BackGray = '#574E52'
fore = 'white'
laranja = '#F25B2A'
cinzaback = '#2D2A2B'

# ========================================= LOGIN DO FUNCIONÁRIO========================================================
def login1():
    f1.forget()
    f2.pack()

def confir_f():
    if ra.get() != raf and sh1.get() != senhaf:
        tkinter.messagebox.showerror("Erro!", "RA ou senha inválidos!")
    else:
        cadastro_cliente()

# =================================FORMATAÇÕES DAS ENTRADAS DO CADASTRO DE CLIENTES=====================================
def format_cpf(event=None):
    text = cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""
    if event.keysym == "BackSpace":
        return
    for i in range(len(text)):
        if text[i].isnumeric():
            if i in [2, 5]:
                new_text += text[i] + "."
            elif i == 8:
                new_text += text[i] + "-"
            else:
                new_text += text[i]
    cpf.delete(0, "end")
    cpf.insert(0, new_text)

def format_data(event=None):
    text = data.get().replace("/", "")[:8]
    new_text = ""
    if event.keysym == "BackSpace":
        return
    for i in range(len(text)):
        if text[i].isnumeric():
            if i in [1, 3]:
                new_text += text[i] + "/"
            else:
                new_text += text[i]
    data.delete(0, "end")
    data.insert(0, new_text)

def format_tel(event=None):
    text = tele.get().replace("(", "").replace(")", "").replace("", "").replace(" ", "")[:13]
    new_text = ""
    if event.keysym == "BackSpace":
        return
    for i in range(len(text)):
        if text[i].isnumeric():
            if i in [0]:
                new_text += "(" + text[i]
            elif i in [2]:
                new_text += text[i] + ")"
            elif i in [3]:
                new_text += " " + text[i] + " "
            elif i in [7]:
                new_text += text[i] + "-"
            else:
                new_text += text[i]
    tele.delete(0, "end")
    tele.insert(0, new_text)

#'AC-','AL-''AM-','BA-','ES-','GO-','MA-','MG-','PA-','RJ-','RS-','SP-','TC-'
def rg_format(event = None):
    text = rg.get().replace(".", "").replace('AC-','').replace('AL-','').replace('AM-','').replace('BA-','').replace('ES-','').replace('GO-','').replace('MA-','').replace('MG-','').replace('PA-','').replace('RJ-','').replace('RS-','').replace('SP-','').replace('TC-','')[:8]
    new_text = ""
    if event.keysym == "BackSpace":
        return
    for i in range(len(text)):
        if text[i].isnumeric():
            if i in [1,4]:
                new_text +=  text[i] +"."
            elif i ==0:
                new_text+= cb.get() + text[i]
            else:
                new_text += text[i]
    rg.delete(0, "end")
    rg.insert(0, new_text)

# ==========================================TELA DE CADASTRO DE CLIENTES================================================
# =========================================Apenas funcionários tem acesso===============================================
def cadastro_cliente():
    f2.forget()
    f4.pack()

# =============================FUNÇÃO PARA ARMAZENAR AS INFORMAÇÕES DOS CLIENTES NO VETOR===============================
lista_cliente = []
lista_contas = []
def armazena():
    global lista_cliente, lista_contas, nome, cpf, data, us1, sh2, a
    lista_cliente.append(Cliente(nome.get(),(cpf.get()),(data.get()),(us1.get()),(sh2.get()),(a)))
    for i in range(len(lista_cliente)):
        if lista_cliente[i].cpf == cpf.get():
            lista_contas.append(Conta(lista_cliente[i]))

# =================================================LOGIN DO CLIENTE=====================================================
def login2():
    f1.forget()
    f3.pack()

def confir_c():
    global lista_contas, us2, sh3
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get() and lista_contas[i].senha == sh3.get():
            menu()
        else:
            tkinter.messagebox.showerror("Erro!", "Usuário ou senha inválidos!")

# ==================================TELA DE MENU DE OPIÇÕES DE OPERAÇÃO BANCÁRIA========================================
def menu():
    f3.forget()
    f5.pack()

def saque():
    f5.forget()
    f6.pack()

def conf_saque():
    global lista_contas, us2
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            lista_contas[i].dados3(float(saqva.get()))
            saldva['text'] = 'Titular: ' + str(lista_contas[i].titular) + '\nNúmero da Conta: ' + str(lista_contas[i].cont) + '\nSaldo: ' + str(lista_contas[i].saldo)

def depos():
    f5.forget()
    f7.pack()

def conf_depos():
    global lista_contas, us2, saldva
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            lista_contas[i].dados2(float(deposva.get()))
            saldva['text'] = 'Titular: ' + str(lista_contas[i].titular) + '\nNúmero da Conta: ' + str(lista_contas[i].cont) + '\nSaldo: ' + str(lista_contas[i].saldo)

def transfe():
    f5.forget()
    f8.pack()

def conf_transf():
    global lista_contas, transfcont, transfva, us2
    for c in range(len(lista_contas)):
        if lista_contas[c].cont == transfcont.get():
            conta_destinatario = lista_contas[c]

    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            lista_contas[i].dados4(float(transfva.get()), conta_destinatario)
            saldva['text'] = 'Titular: ' + str(lista_contas[i].titular) + '\nNúmero da Conta: ' + str(lista_contas[i].cont) + '\nSaldo: ' + str(lista_contas[i].saldo)

def extrato():
    f5.forget()
    global lista_contas, us2, extrava
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            lista_contas[i].dados5()
            extrava['text'] = lista_contas[i].historico.mostrar
    f9.pack()
    
def imprime():
    global lista_contas, us2
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            lista_contas[i].dados6()

def saldo():
    f5.forget()
    global lista_contas, us2
    for i in range(len(lista_contas)):
        if lista_contas[i].usuario == us2.get():
            saldva['text'] = 'Titular: ' + str(lista_contas[i].titular) + '\nNúmero da Conta: ' + str(lista_contas[i].cont) + '\nSaldo: ' + str(lista_contas[i].saldo)
    f10.pack()

# ================================================JANELA PRINCIPAL======================================================
primeira = Tk()
primeira.title('Seleção')
primeira.geometry('990x600+200+200')
primeira.resizable(width=False, height=False)

#======================= ======================================================================
#primeira.bind('<Button-1>', posiciona.inicio_place)
#primeira.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, primeira))
#primeira.bind('<Button-2>', lambda arg: posiciona.para_geometry(primeira))

#======================= FRAME 1 =======================================
telainicial = PhotoImage(file='layout_img/inicial.png')

btfuncio  = PhotoImage(file='layout_img/btfunc.png')

btclient = PhotoImage(file='layout_img/btClient.png')

#======================= FRAME 2=======================================
telafuncio = PhotoImage(file='layout_img/loginF.png')

btentrar = PhotoImage(file='layout_img/btentrar.png')

btvoltarL = PhotoImage(file='layout_img/voltarL.png')

#======================= FRAME 3 =======================================
telaclient = PhotoImage(file='layout_img/loginC.png')

btvoltarC = PhotoImage(file='layout_img/voltarC.png')

#======================= FRAME 4 =======================================
telacadas = PhotoImage(file='layout_img/cadastroC.png')

btsalvar = PhotoImage(file='layout_img/btsalvar.png')

btnovac = PhotoImage(file='layout_img/btnovac.png')

#======================= FRAME 5=======================================
telamenu = PhotoImage(file='layout_img/menu.png')

bde = PhotoImage(file='layout_img/Botão_de_Depósito_menu.png')

be = PhotoImage(file='layout_img/Botão_de_extrato_menu.png')

bs = PhotoImage(file='layout_img/Botão_de_saldo_menu.png')

bsa = PhotoImage(file='layout_img/Botão_de_Saque_menu.png')

bt = PhotoImage(file='layout_img/Botão_de_Transferência_menu.png')

#======================= FRAME 6 =======================================
btsaq = PhotoImage(file='layout_img/btsacar.png')

telasaque = PhotoImage(file='layout_img/saque.png')

#======================= FRAME 7 =======================================
btde = PhotoImage(file='layout_img/btdep.png')

teladep = PhotoImage(file='layout_img/dep.png')

#======================= FRAME 8 =======================================
telatranf = PhotoImage(file='layout_img/transf.png')

bttransferir = PhotoImage(file='layout_img/Botão_Transferir.png')

#======================= FRAME 9 =======================================
btex = PhotoImage(file='layout_img/btimprimir.png')

telaextra = PhotoImage(file='layout_img/extrato.png')

#======================= FRAME 10 =======================================
telasaldo = PhotoImage(file='layout_img/saldo.png')

# ===============================================CRIAÇÃO DE FRAMES======================================================
f1 = Frame(primeira)
f1.pack()
f2 = Frame(primeira)
f3 = Frame(primeira)
f4 = Frame(primeira)
f5 = Frame(primeira)
f6 = Frame(primeira)
f7 = Frame(primeira)
f8 = Frame(primeira)
f9 = Frame(primeira)
f10 = Frame(primeira)
f11 = Frame(f8)

#================================================== import animation==========================================================]
AnimaCnt = 12
Anima = [PhotoImage(file='layout_img/load.gif', format= 'gif -index %i' %(i)) for i in range(AnimaCnt)]

def update(ind):
    porc = Anima[ind]
    ind += 1
    if ind == AnimaCnt:
        ind = 0
    anima.configure(image=porc)
    f11.after(100, update, ind)
anima = Label(f11)
anima.pack()
anima.after(0, update, 0)

# =====================================DEFINIR IMAGEM DE FUNDO DO PRIMEIRO FRAME========================================
lab_inicial = Label(f1, image=telainicial)
lab_inicial.pack()

# ============================================WIDGETS DO PRIMEIRO FRAME=================================================
b1 = Button(f1, image=btfuncio, bd=0, command=login1)
b1.place(width=226, height=97, x=662, y=288)
b2 = Button(f1, image=btclient, bd=0, command=login2)
b2.place(width=229, height=94, x=660, y=414)

# =====================================DEFINIR IMAGEM DE FUNDO DO SEGUNDO FRAME=========================================
lab_login1 = Label(f2, image=telafuncio)
lab_login1.pack()

# ============================================WIDGETS DO SEGUNDO FRAME==================================================
#,loading.pack(),loading.after(000,loading.update()),loading.forget()
ra = Entry(f2, font=("Calibri", 15), background=BackGray, foreground=fore, bd=0, justify=CENTER)
ra.place(width=324, height=28, x=370, y=208)
sh1 = Entry(f2, font=("Calibri", 15), background=BackGray, foreground=fore, bd=0, justify=CENTER, show='*')
sh1.place(width=273, height=27, x=420, y=315)
b3 = Button(f2, image=btentrar, bd=0, command=confir_f)
b3.place(width=260, height=105, x=363, y=439)
b4 = Button(f2, image= btvoltarL, bd=0, command=lambda: [f2.forget(), f1.pack()])
b4.place(width=88, height=78, x=18, y=18)

# ======================================DEFINIR IMAGEM DE FUNDO DO QUARTO FRAME=========================================
lab_cadastro = Label(f4, image=telacadas)
lab_cadastro.pack()

# =============================================WIDGETS DO QUARTO FRAME==================================================
nome = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
nome.place(width=395, height=24, x=225, y=133)

cpf = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
cpf.bind("<KeyRelease>", format_cpf)
cpf.place(width=165, height=18, x=539, y=169)

#=====================================================MENU DO RG==========================================================
estados =['AC-','AL-','AM-','BA-','ES-','GO-','MA-','MG-','PA-','RJ-','RS-','SP-','TC-']
cb = ttk.Combobox(f4,values=estados)
cb.set('MG-')
cb.place(width=50, height=27, x=942, y=159)
rg = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
rg.bind("<KeyRelease>", rg_format)
rg.place(width=168, height=22, x=772, y=166)

data = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
data.bind("<KeyRelease>", format_data)
data.place(width=172, height=30, x=777, y=126)

tele = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
tele.bind("<KeyRelease>", format_tel)
tele.place(width=246, height=18, x=706, y=204)

email = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0 ,justify=CENTER)
email.place(width=434, height=19, x=125, y=204)

radioVale = tkinter.IntVar()
se1 = Radiobutton(f4, bd=0,fg=laranja,bg=cinzaback, variable=radioVale, value=1)
se1.place(width=20, height=22, x=320, y=175)

se2 = Radiobutton(f4,fg=laranja,bg=cinzaback, bd=0,variable=radioVale, value=2)
se2.place(width=20, height=22, x=157, y=175)

rua = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
rua.place(width=479, height=25, x=91, y=263)

num = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0, justify=CENTER)
num.place(width=136, height=25, x=633, y=262)

bai = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
bai.place(width=252, height=20, x=466, y=300)

cidi = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
cidi.place(width=223, height=23, x=127, y=332)

est = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
est.place(width=214, height=23, x=466, y=333)

cep = Entry(f4, font=("Calibri", 15),background=cinzaback,foreground=fore,bd=0, justify=CENTER)
cep.place(width=249, height=20, x=103, y=301)

us1 = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
us1.place(width=217, height=27, x=133, y=399)

sh2 = Entry(f4, font=("Calibri", 15), background=cinzaback,foreground=fore,bd=0,justify=CENTER)
sh2.place(width=163, height=27, x=467, y=397)

def conta():
    global cont, a
    cont = Label(f4,background=cinzaback,foreground=fore, font='Arial 20',text="00"+str(randint(1,99999)))
    cont.place(width=211, height=21, x=740, y=443)
    a = cont['text']

#---------------------------------------------------------------------
b15 = Button(f4, image=btnovac,bd=0, command=conta)
b15.place(width=157, height=65, x=778, y=483)

b5 = Button(f4, image=btsalvar,bd=0,command=armazena)
b5.place(width=262, height=108, x=197, y=468)

b8 = Button(f4, image=btvoltarL,bd=0, command=lambda: [f4.forget(), f2.pack()])
b8.place(width=88, height=78, x=18, y=18)

# ======================================DEFINIR IMAGEM DE FUNDO DO TERCEIRO FRAME=======================================
lab_login2 = Label(f3, image=telaclient)
lab_login2.pack()

# ============================================WIDGETS DO TERCEIRO FRAME=================================================
us2 = Entry(f3, font=("Calibri", 15), background=BackGray, foreground=fore, bd=0, justify=CENTER)
us2.place(width=298, height=26, x=396, y=210)

sh3 = Entry(f3, font=("Calibri", 15), background=BackGray, foreground=fore, bd=0, justify=CENTER, show='*')
sh3.place(width=275, height=28, x=420, y=314)

b6 = Button(f3, image=btentrar, bd=0, command=confir_c)
b6.place(width=263, height=112, x=362, y=434)

b7 = Button(f3, image=btvoltarC, bd=0, command=lambda: [f3.forget(), f1.pack()])
b7.place(width=88, height=78, x=18, y=18)

# =======================================DEFINIR IMAGEM DE FUNDO DO QUINTO FRAME========================================
lab_menu = Label(f5, image=telamenu)
lab_menu.pack()

# =============================================WIDGETS DO QUINTO FRAME==================================================
b9 = Button(f5, image=bsa, bd=0, command=saque)
b9.place(width=227, height=148, x=652, y=148)

b10 = Button(f5, image=bde, bd=0, command=depos)
b10.place(width=320, height=146, x=161, y=322)

b11 = Button(f5, image=bt, bd=0, command=transfe)
b11.place(width=322, height=144, x=534, y=322)

b12 = Button(f5, image=be, bd=0, command=extrato)
b12.place(width=220, height=143, x=390, y=152)

b13 = Button(f5, image=bs, bd=0, command=saldo)
b13.place(width=221, height=147, x=124, y=150)

b14 = Button(f5, image=btvoltarC, bd=0, command=lambda: [f5.forget(), f3.pack()])
b14.place(width=88, height=78, x=18, y=18)

# ======================================DEFINIR IMAGEM DE FUNDO DO SEXTO FRAME==========================================
lab_saque = Label(f6, image=telasaque)
lab_saque.pack()

# =============================================WIDGETS DO SEXTO FRAME===================================================
saqva = Entry(f6, font=("Calibri", 15), bd=0, justify=CENTER)
saqva.place(width=435, height=35, x=277, y=298)

saq = Button(f6, image=btsaq, bd=0, command=conf_saque)
saq.place(width=261, height=104, x=367, y=442)

saqv = Button(f6, image=btvoltarL, bd=0, command=lambda: [f6.forget(), f5.pack()])
saqv.place(width=88, height=78, x=18, y=18)

# =====================================DEFINIR IMAGEM DE FUNDO DO SETIMO FRAME==========================================
lab_depos = Label(f7, image=teladep)
lab_depos.pack()

# ============================================WIDGETS DO SETIMO FRAME===================================================
deposva = Entry(f7, font=("Calibri", 15), bd=0, justify=CENTER)
deposva.place(width=435, height=35, x=277, y=298)

deposit = Button(f7, image=btde, bd=0, command= conf_depos)
deposit.place(width=262, height=103, x=370, y=442)

deposv = Button(f7, image=btvoltarL, bd=0, command=lambda: [f7.forget(), f5.pack()])
deposv.place(width=88, height=78, x=18, y=18)

# =====================================DEFINIR IMAGEM DE FUNDO DO OITAVO FRAME==========================================
lab_transfe = Label(f8, image=telatranf)
lab_transfe.pack()

# =============================================WIDGETS DO OITAVO FRAME==================================================
transfva = Entry(f8, font=("Calibri", 15), bd=0, justify=CENTER)
transfva.place(width=435, height=35, x=277, y=216)

transfcont = Entry(f8, font=("Calibri", 15), bd=0, justify=CENTER)
transfcont.place(width=435, height=35, x=277, y=345)

transf = Button(f8, image=bttransferir, bd=0, command=conf_transf)
transf.place(width=258, height=106, x=368, y=441)

transfv = Button(f8, image=btvoltarL, bd=0, command=lambda: [f8.forget(), f5.pack()])
transfv.place(width=88, height=78, x=18, y=18)

# ======================================DEFINIR IMAGEM DE FUNDO DO NONO FRAME===========================================
lab_extrato = Label(f9, image=telaextra)
lab_extrato.pack()

# =============================================WIDGETS DO NONO FRAME====================================================
extrava = Label(f9, text='', background=BackGray, foreground=fore, bd=0)
extrava.place(width=441, height=210, x=275, y=167)

extra = Button(f9, image=btex, bd=0, command=imprime)
extra.place(width=263, height=107, x=369, y=441)

extrav = Button(f9, image=btvoltarL, bd=0, command=lambda: [f9.forget(), f5.pack()])
extrav.place(width=88, height=78, x=18, y=18)

# ======================================DEFINIR IMAGEM DE FUNDO DO DECIMO FRAME=========================================
lab_saldo = Label(f10, image=telasaldo)
lab_saldo.pack()

# ===========================================WIDGETS DO DECIMO FRAME====================================================
saldva = Label(f10, text='', font='Arial 15', background=BackGray, foreground=fore, bd=0)
saldva.place(width=442, height=298, x=272, y=173)

saldv = Button(f10, image=btvoltarL, bd=0, command=lambda: [f10.forget(), f5.pack()])
saldv.place(width=88, height=78, x=18, y=18)

primeira.mainloop()
