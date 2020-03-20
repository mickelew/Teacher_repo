tal_1 = int(input("Skriv in ett tal: "))
tal_2 = int(input("Skriv in ytterligare ett tal: "))
summa_var =tal_1+tal_2
differens_var =tal_1-tal_2
produkt_var =tal_1*tal_2
kvot_var =tal_1 // tal_2
print("\nSumman av",tal_1,"och",tal_2,"är",summa_var)
print("\nDifferensen mellan %d och %d är %d" %(tal_1, tal_2, differens_var))
print("\nProdukten av {tal1_var} och {tal2_var} är {produkt}." .format(tal1_var=tal_1, tal2_var=tal_2, produkt=produkt_var))
print(f"\nKvoten av {tal_1} och {tal_2} är {kvot_var}.")