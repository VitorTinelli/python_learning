print ("-_-_- Calculadora de aposentadoria do Omega -_-_-") 
print ()
codfun = int(input("Digite o código do funcionário: "))
datnas = int(input("Digite seu ano de nascimento: "))
dating = int(input("Digite o ano de ingresso na empresa: "))

idade = 2023 - datnas

if idade >= 65 or 2023 - dating >= 30 or idade >=60 and 2023 - dating >= 25:
    print("Requerer aposentadoria.")
else: 
    print("Não requerer aposentadoria.")