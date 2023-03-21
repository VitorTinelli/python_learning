print ("-_-_- Calculadora de votação em ladrão do Omega -_-_-")
print ()
nbranco =int(input("Digite o número de votos em branco: "))
nnulo = int(input("Digite o número de votos nulos: "))
nval = int(input("Digite o número de votos válidos: "))

ntot = nbranco + nnulo + nval
print ("Porcentagem de votos nulos: {:.2f}%".format(nbranco/ntot*100))
print ("Porcentagem de votos nulos: {:.2f}%".format(nnulo/ntot*100))
print ("Porcentagem de votos nulos: {:.2f}%".format(nval/ntot*100))
print()
print()