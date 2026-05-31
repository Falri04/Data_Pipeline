# Pandas Data Analysis Crash Course (Bestelldaten)

Ein kompaktes Python-Skript, das die wichtigsten Kernfunktionen der **Pandas**-Bibliothek zur Datenanalyse demonstriert. Anhand eines praktischen Beispiels mit fiktiven Bestelldaten werden das Laden von Daten, die statistische Auswertung, das Filtern sowie das Gruppieren von Daten veranschaulicht.

## Hauptfunktionen des Skripts

Das Skript ist in vier logische Schritte unterteilt, die den typischen Workflow einer Datenanalyse abbilden:

1. **Daten laden & Überblick verschaffen:** * Erstellung eines DataFrames aus Rohdaten (simuliert eine bereinigte CSV-Datei).
   * Nutzung von `.head(n)` zur schnellen Sichtung der ersten Datensätze.
   * Nutzung von `.describe()` zur automatischen Berechnung statistischer Kennzahlen (Mittelwert, Minimum, Maximum etc.) für finanzielle Beträge.

2. **Daten filtern (Slicing):** * Filterung des Datensatzes nach bestimmten Kriterien (z. B. Identifikation aller Bestellungen mit einem Warenwert von über 80,00 EUR).

3. **Daten gruppieren & aggregieren (Group By):** * Segmentierung der Daten nach Geschäftsbereichen (`Bereich`), um den Gesamtumsatz pro Kategorie zu ermitteln.

4. **Visualisierung (optional):** * Vorbereiteter Code zur Erstellung eines einfachen Balkendiagramms (Bar Chart) für die Umsatzverteilung.

## Voraussetzungen & Installation

Um das Skript lokal auszuführen, benötigst du **Python 3** sowie die Bibliothek **Pandas**. Optional wird **Matplotlib** für die Diagrammdarstellung benötigt.

Installiere die benötigten Pakete einfach über dein Terminal:

```bash
pip install pandas matplotlib
