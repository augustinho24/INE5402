#Conversão de idade em dias para anos, meses e dias.
#

i = int(input())

anos = i // 365
minutos = (i % 365) // 30 
dias = (i % 365) % 30 

print(f"{anos} ano(s)")
print(f"{minutos} mes(es)")
print(f"{dias} dia(s)")
