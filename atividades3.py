#for: É usado quando você já sabe a quantidade de vezes que o bloco de codigo deve ser repetido.
# é mais vantajoso para automatizar tarefas com limites fixos

#while: É usado quando você não sabe quantas vezes a repetição vai acontecer.
# é mais vantajoso para situações imprevistas

#QUESTAO 22

vida = 5

while vida > 0:
    print("Você ainda está jogando")
    vida = vida - 1

#QUESTAO 23

for i in range(1, 6):
    print(f"Numero: {i}")

#QUESTAO 24

#range(4) gera os numeros 0, 1, 2, 3
#range(2, 6) gera os numeros 2, 3, 4, 5, 6
#range(0, 10, 12)gera os numeros 0, 2, 4, 6, 8

#QUESTAO 25
contador = 1
while contador <= 5:
    print("o numero é:", contador)
    contador = contador + 1

#QUESTAO 26
for i in range(1, 5):
    print(i)

#QUESTAO 27

tempo = 10

while tempo >= 0:
    print(tempo)
    tempo = tempo - 1

print("Fogo")

#QUESTAO 28

senha = ""

while senha != "ifc123":
    senha = input("digite sua senha de acesso: ")

print("Acesso liberado")

#QUESTAO 29
