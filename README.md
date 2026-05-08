# Správa filmov

Aplikácia na správu filmov s možnosťou ručného pridávania a vyhľadávania cez OMDb API.

## Požiadavky

- Python 3.6 alebo novší
- Účet na [OMDb API](https://www.omdbapi.com/apikey.aspx) pre získanie API kľúča

## Inštalácia

1. Naklonuj repozitár:
    ```bash
   git clone https://github.com/majacab55-ui/Sprava-filmov.git
   cd Sprava-filmov
   ```

2. Vytvor konfiguračný súbor z vzoru:
    ```bash
   cp .env.example .env
   ```

3. Otvor súbor .env a vlož svoj API kľúč:
    ```bash
   OMDB_API_KEY=tvoj_skutocny_api_kluc
   ```

4. Nainštaluj závislosti:
    ```bash
   pip install requests python-dotenv
   ```

5. Spusti aplikáciu:
    ```bash
   python main.py
   ```

## Štruktúra

- `movie.py` – trieda Movie s validáciou a zapuzdrením
- `api.py` – komunikácia s OMDb API
- `manager.py` – správa zoznamu a perzistencia (JSON)
- `input_utils.py` – validované vstupy od užívateľa
- `main.py` – hlavné menu
- `.env.example` – vzor konfiguračného súboru
- `movies.json` – databáza filmov (vytvorí sa automaticky)

## Funkcie

- Pridať film ručne (s kontrolou vstupov)
- Pridať film z API (s chybovými hláškami)
- Vyhľadať film podľa názvu a filtrovanie filmov
- Zobraziť všetky filmy
- Automatické ukladanie do `movies.json`
