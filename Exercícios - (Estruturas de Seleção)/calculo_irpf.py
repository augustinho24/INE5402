sal_bruto = float(input())
dependentes = int(input())

inss = 0

desconto_dependentes = 137.99 * dependentes


if sal_bruto <= 1372.81:
    
    if sal_bruto <= 720.00:
        inss = sal_bruto * 0.0765
    elif sal_bruto <= 1200.00:
        inss = sal_bruto * 0.09
    else:
        inss = sal_bruto * 0.11

    irpf = (sal_bruto - desconto_dependentes - inss) * 0
    print(f"{irpf:.2f}")
    

elif sal_bruto <= 2743.25:
    
    if sal_bruto <= 2400.00:
        inss = sal_bruto * 0.11
    else:
        inss = 2400 * 0.11
    
    irpf = ((sal_bruto - desconto_dependentes - inss) * 0.15) - 205.92
    if irpf < 0:
        irpf = 0    
    print(f"{irpf:.2f}")
    
else:
    
    inss = 2400 * 0.11
    
    irpf = ((sal_bruto - desconto_dependentes - inss) * 0.275) - 548.82
    
    if irpf < 0:
        irpf = 0
    print(f"{irpf:.2f}")
        
    
    
    

