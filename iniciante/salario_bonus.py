nome=str(input())
s_fixo= float(input())
vendas_RS= float(input())

montante= vendas_RS*0.15
total= montante+s_fixo

print("TOTAL = R$ {:.2f}".format(total))