print ("-_-_- Calculadora de permissão para votar do Omega -_-_-")
print ()
anoatu =int(input("Digite o ano atual: "))
anonasc = int(input("Digite o ano de seu nascimento: "))

idade = anoatu - anonasc

if idade <16:
    print("Você não pode votar!")
else : print("Você pode votar caso tenha o título de eleitor.")
print()
print()