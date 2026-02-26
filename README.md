# Weather ETL Pipeline

Weather ETL Pipeline je Python projekat koji demonstrira kompletan ETL proces: izvlačenje, transformaciju i učitavanje podataka o vremenu.  
Podaci o gradovima (sa koordinatama) se uzimaju iz CSV fajla, proširuju trenutnim podacima sa Open-Meteo API-ja, sortiraju po temperaturi i generišu osnovne statistike.

---

## Struktura projekta

- `extract.py` – funkcije za učitavanje CSV fajlova  
- `transform.py` – funkcije za obogaćivanje podataka, mapiranje weather code-a i generisanje statistika  
- `load.py` – funkcije za snimanje obrađenih CSV fajlova  
- `main.py` – pokreće ceo ETL pipeline  
- `data/` – sadrži ulazni CSV (`gradovi.csv`) i izlazne fajlove (`gradovi_produzeno.csv`, `gradovi_stats.csv`)  

---

## Funkcionalnosti

- Učitavanje gradova iz CSV-a  
- Dohvatanje trenutnih podataka o vremenu preko Open-Meteo API-ja  
- Pretvaranje numeričkog weather code-a u opis (npr. `0 -> Clear sky`)  
- Dodavanje kolona: `temperature`, `windspeed`, `weathercode`  
- Sortiranje po temperaturi  
- Generisanje statistika: minimum, maksimum i prosečna temperatura  

---

## Instalacija i pokretanje

1. Kloniraj repozitorijum:

```bash
git clone https://github.com/VukasinJ-dev/weather_etl.git
cd weather_etl
```

2. Instaliraj potrebne biblioteke
```bash
pip install -r requirements.txt
```

3.Pokreni program:
```bash
python main.py
```
