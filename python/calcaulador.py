"""
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("escolha uma operação:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operacao = int(input("Digite a operação: "))

if operacao == 1:
    print(numero1 + numero2)
elif operacao == 2:
    print(numero1 - numero2)
elif operacao == 3:
    print(numero1 * numero2)
elif operacao == 4:
    print(numero1 / numero2)
else:
    print("Operação inválida")

"""

def button_press(num):
    pass
def equals():
    pass
def clear():
    pass

window = Tk()
window.title("Calculadora")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()
equation_label.set(window,textvariable=equation_label,font=("consolas",20),bg="white",width=24,height=2)

label.pack()

frame  = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,command=lambda: button_press(1))
button1.grid(row=0,column=0)
button2 = Button(frame,text=2,height=4,width=9,font=35,command=lambda: button_press(2))
button2.grid(row=0,column=1)
button3 = Button(frame,text=3,height=4,width=9,font=35,command=lambda: button_press(3))
button3.grid(row=0,column=2)
button4 = Button(frame,text=4,height=4,width=9,font=35,command=lambda: button_press(4))
button4.grid(row=1,column=0)






window.mainloop()
