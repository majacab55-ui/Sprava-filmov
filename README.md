# Správa filmov

Aplikácia na správu filmov s možnosťou ručného pridávania a vyhľadávania cez OMDb API.

## Inštalácia

1. Naklonuj repozitár.
2. Vytvor `.env` súbor s kľúčom: `OMDB_API_KEY=tvoj_kluc`
3. Nainštaluj závislosti: `pip install requests`
4. Spusti: `python main.py`

## Štruktúra

- `movie.py` – trieda Movie s validáciou a zapuzdrením
- `api.py` – komunikácia s OMDb API
- `manager.py` – správa zoznamu a perzistencia (JSON)
- `input_utils.py` – validované vstupy od užívateľa
- `main.py` – hlavné menu

## Funkcie

- Pridať film ručne (s kontrolou vstupov)
- Pridať film z API (s chybovými hláškami)
- Vyhľadať film podľa názvu
- Zobraziť všetky filmy
- Automatické ukladanie do `movies.json`
