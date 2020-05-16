numeros= [1,5,3]
length = len(numeros)
valores = []
valores_str = ""
s = 0
	
#Colocando os valores ^ ao length dentro de um array
for i in range(length):
    valores.append((numeros[i] ** length))
    #print(valores)

#Somando valores 
for i in range (len(valores)):
    s = valores[i] + s
    #print(s)

# Convertendo os valores do array incial em String
for i in range(len(numeros)):
    valores_str =  valores_str + str(numeros[i]) 
#print(valores_str)

#Verificando se é um número de Armstrong
if valores_str == str(s):
   print("true")

else:
    print("false")