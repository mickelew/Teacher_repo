print("Detta program räknar ut hur många dagar, timmar, minuter och sekunder det går på givet antal sekunder.")
input_sekunder = int(input("Skriv antal sekunder: "))
sekunder_pa_en_dag = 60*60*24
antal_dagar = input_sekunder // sekunder_pa_en_dag
print(f"Antal dagar: {antal_dagar}")
sekunder = input_sekunder % sekunder_pa_en_dag
sekunder_pa_en_timme = 60 * 60
antal_timmar = sekunder // sekunder_pa_en_timme
print(f"Antal timmar: {antal_timmar}")
sekunder = sekunder % sekunder_pa_en_timme
print(f"Antal sekunder: {sekunder}")