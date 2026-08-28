"""
#1 

salary_brute = int(input("Digite o seu salario bruto: "))
percent_bonus = 0.1 * salary_brute
liquid_salary = salary_brute + percent_bonus
print(f"Seu salario bruto eh: {salary_brute}")
print(f"Seu salario liquido eh: {liquid_salary}")


#2
werehouse = int(input("Digite a quantidade de produtos: "))
sells = int(input("Digite a quantidade de vendas: "))
reload = int(input("Digite a quantidade de produtos recarregados    : "))
new_werehouse = werehouse - sells + reload
print(f"Quantidade de produtos no estoque: {new_werehouse}")

#3
box = 1250
truck = 12 

tracker = box // truck
rest = box % truck
print(f"Quantidade de caixas por caminhão: {tracker}")
print(f"Quantidade de caixas sobrando: {rest}")

#4
faturamento = 15000
custo = 5000
tax = 0.15

imposto = faturamento * tax
lucro = faturamento - custo - imposto
margem = lucro / faturamento

print(f"O imposto eh: {imposto}")
print(f"O lucro eh: {lucro}")
print(f"A margem eh: {margem}")

meta_atingida = margem > 0.3
print(f"Meta atingida: {meta_atingida}")
    
#5 
contrato = 40 
contratos_anos = 40 // 12
contratos_meses = 40 % 12

print(f"Anos: {contratos_anos}")
print(f"Meses: {contratos_meses}")

#6
email = "alessandro@empresa.com.br"
new_email = "@jobsfider.com.br"
email = email.split("@")
emailuser = email[0] + new_email

print(emailuser)

#7
email = "uWVg1@example.com"
position = email.find("@")
username = email[:position]
print(username)

#8
mensagem = "Ola [nome] seja bem vindo ao curso de python"
nome = input("Digite seu nome completo : ")
primeiro_nome = nome[:nome.find(" ")]

mensagem = mensagem.replace("[nome]", primeiro_nome)
print(mensagem)

#9
sells = [1500 , 2000, 3000, 4000, 5000]
total = 0
for sell in sells:
    total += sell

print(f"O total de vendas eh: {total:.2f}")
print(f'A media de vendas eh: {total / len(sells)}')
print(f'A maior venda eh: {max(sells)}')
print(f'A menor venda eh: {min(sells)}')

#10
products = ["mouse", "teclado", "monitor", "gabinete"]
products.append("mousepad")
position = products.index("mouse")
products[position] = "mouse gamer"
print(products)

#11
freighs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

freighs.sort()
print(f"Maior frete: {freighs[-1]}")
print(f"O segundo maior frete: {freighs[-2]}")
freighs
#12 
city_track = ["Rio de Janeiro", "Sao Paulo", "Salvador", "Curitiba", "Fortaleza"]
new_tracker = ["Toledo", "Belo Horizonte", "Manaus"]
city_track.extend(new_tracker)
postion_salvador = city_track.index("Salvador")+1

print(city_track)
print(f"Posicao de Salvador: {postion_salvador} " )
#13
price = [100 , 200 , 300]
wines = ["Vinho 1" , "Vinho 2" , "Vinho 3"]

wine_choosen = input("Escolha um vinho: ")
try:
    position = wines.index(wine_choosen)
except ValueError:
    print("O vinho escolhido não está na lista.")
    exit()

new_price = int(input("Digite o novo preco: "))
price[position] = new_price
print(price)
"""
#14 

performance = {"A": [10,7,5] , "B": [7,5,3] , "C": [5,3,1]}

nome = input("Digite o nome do atleta: ")
socore =  performance[nome]
print(f"O atleta {nome} tirou {socore} pontos")

media = sum(socore) / len(socore)
print(f"A media do atleta {nome} eh {media}")