from tkinter import *

#variavel temporaria para usar os botoes
resulttemp = ''

#funcao para atualizar os numeros em tela
def mudaresult(num):
  global resulttemp
  resulttemp = resulttemp + str(num)
  equa.set(resulttemp)

#funcao para mostrar o resultado
def pronto():
  #tenta resolver                                     
  try:
    global resulttemp
    #funcao eval retorna o resultado da expressao  
    total=str(eval(resulttemp))
    equa.set(total)
    resulttemp =''
  #caso nao der certo, seta o resultado como erro
  except:
    equa.set('erro')
    resulttemp =''
    
#funcao para limpar os numeros na tela    
def limpa():
  global resulttemp
  equa.set('')
  resulttemp =''

#inicializa o loop do tkinter
root = Tk()
root.geometry('320x500')
root.title('Calculadora')
root.resizable(width=False,height=False)


#cria todos os botoes 
igual = Button(root, text='=', command=pronto, height = 3, width = 7)
mais= Button(root, text='+', command=lambda: mudaresult('+'), height = 3, width = 7)
menos= Button(root, text='-', command=lambda: mudaresult('-'), height = 3, width = 7)
multiplaca= Button(root, text='x',command=lambda: mudaresult('*'), height = 3, width = 7)
divisao= Button(root, text='/', command=lambda: mudaresult('/'), height = 3, width = 7)
virgula = Button(root, text='.', command=lambda: mudaresult('.'), height = 3, width = 7)
zero = Button(root, text= '0', command=lambda: mudaresult(0), height = 3, width = 7)
um = Button(root, text= '1', command=lambda: mudaresult(1), height = 3, width = 7)
dois = Button(root, text= '2', command=lambda: mudaresult(2), height = 3, width = 7)
tres = Button(root, text= '3', command=lambda: mudaresult(3), height = 3, width = 7)
quatro = Button(root, text= '4', command=lambda: mudaresult(4), height = 3, width = 7)
cinco = Button(root, text= '5', command=lambda: mudaresult(5), height = 3, width = 7)
seis = Button(root, text= '6', command=lambda: mudaresult(6), height = 3, width = 7)
sete = Button(root, text= '7', command=lambda: mudaresult(7), height = 3, width = 7)
oito = Button(root, text= '8', command=lambda: mudaresult(8), height = 3, width = 7)
nove = Button(root, text= '9', command=lambda: mudaresult(9), height = 3, width = 7)
apaga = Button(root, text='C', command=limpa, height = 3, width = 7)

#colocando os botoes por cordenadas na tela
igual.place(x=262, y=445)
virgula.place(x=204, y=445)
mais.place(x=262, y=389)
menos.place(x=262, y=333)
multiplaca.place(x=262, y=277)
divisao.place(x=262,y=222)
zero.place(x=147, y=445)
um.place(x=89, y=389)
dois.place(x=147, y=389)
tres.place(x=204, y=389)
quatro.place(x=89, y=333)
cinco.place(x=147, y=333)
seis.place(x=204, y=333)
sete.place(x=89, y=277)
oito.place(x=147, y=277)
nove.place(x=204, y=277)
apaga.place(x=89,y=445)

#equa e oque aparece dentro da caixa de texto da tela
equa = StringVar()

#criando e colocando a caixa de texto da tela
resultado=Entry(root, textvariable=equa)
resultado.place(x=103,y=104)

#termina o loop
root.mainloop()


