# Reajuste de salário

sal_individual = float(input())
sal_min = float(input())

coef_sal = sal_individual/sal_min

if (coef_sal <= 3):
    reajuste = sal_individual + (sal_individual*0.2)    
elif (coef_sal <= 5):
    reajuste = sal_individual + (sal_individual*0.15)
else:
    reajuste = sal_individual + (sal_individual*0.1)
    
if reajuste < (sal_min * 1.5):
    reajuste = sal_min * 1.5

elif reajuste > (sal_min * 20):
    reajuste = sal_min * 20


print(f"{reajuste:.2f}")

    
    
    