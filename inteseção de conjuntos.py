a = list()
b= list()
c= list()
perguntas = int(input("Quantos numeros você quer para o CONJUNTO A: "))

for n in range(perguntas):
    qst2 = int(input("Elemento: "))
    a.append(qst2)

perguntas_b = int(input("Quantos numeros você quer para o CONJUNTO B: "))

for num in range(perguntas_b):
    qst3 = int(input("Elemento: "))
    b.append(qst3)

for element in a:
    if element in b:
        c.append(element)

print(f"O conjunto A interseção B é {c}")