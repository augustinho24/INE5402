#Custo de locação de veículo

dias_uso = int(input("Dias de uso: "))
km_rodados = float(input("Km rodados: "))
km_rodados_dia = km_rodados / dias_uso


if km_rodados_dia > 60:
    custo = (((45.00 * dias_uso) + (((km_rodados_dia - 60) * 0.5) * dias_uso)))
    print(f"{custo:.2f}")
else:
    custo = dias_uso * 45.00  
    print(f"{custo:.2f}")