import pandas as pd

# 1. DATEN LADEN & ÜBERBLICK VERSCHAFFEN
# Wir erstellen das DataFrame (simuliert unsere saubere CSV-Datei)
data = {
    'Bestell_ID': [101, 103, 105, 106, 107],
    'Kunde': ['Anna', 'Chris', 'Eva', 'Ben', 'Anna'],
    'Bereich': ['Elektronik', 'Bücher', 'Elektronik', 'Garten', 'Bücher'],
    'Betrag_EUR': [120.00, 73.60, 87.40, 45.00, 30.00]
}
df = pd.DataFrame(data)

print("--- DIE ERSTEN ZEILEN ANSCHAUEN ---")
# .head(n) zeigt dir die ersten n Zeilen deiner Tabelle
print(df.head(3)) 

print("\n--- SCHNELLE STATISTIK (.describe) ---")
# .describe() berechnet automatisch Mittelwert, Min, Max etc. für alle Zahlen
print(df['Betrag_EUR'].describe())


# 2. DATEN FILTERN (Slicing)
print("\n--- FILTER: Bestellungen über 80 EUR ---")
# Wir erstellen eine Bedingung und wenden sie auf das DataFrame an
teure_bestellungen = df[df['Betrag_EUR'] > 80]
print(teure_bestellungen)


# 3. DATEN GRUPPIEREN & AGGREGRIEREN (Group By)
print("\n--- UMSATZ NACH BEREICH ---")
# Welcher Bereich bringt den meisten Umsatz? 
# Wir gruppieren nach 'Bereich' und summieren die Beträge
umsatz_nach_bereich = df.groupby('Bereich')['Betrag_EUR'].sum()
print(umsatz_nach_bereich)


# 4. EINFACHE VISUALISIERUNG (Optional, braucht matplotlib)
#df.groupby('Bereich')['Betrag_EUR'].sum().plot(kind='bar')