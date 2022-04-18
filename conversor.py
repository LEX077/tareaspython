soles = input("¿Cuantos soles peruanos tienes?: ")
soles = float(soles)
valor_dolar_sunat_17_abril_2022 = 3.77
dolares = soles / valor_dolar_sunat_17_abril_2022
dolares = round(dolares, 3)
dolares = str(dolares)
print("tiens $" + dolares)
