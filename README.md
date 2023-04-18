# Coop-Vr-Controlpanel

Dette er et webbaseret kontrolpanel til Coop-Vr. Det er lavet i Flask og Python. 

## Installation
setup er lavet til at installere alt hvad der skal bruges til at køre programmet.

## Krav
* Python 3.5 eller nyere (kan downloades [her](https://www.python.org/downloads/))
## Kør programmet

### Windows
1. Åben en terminal i mappen med setup.py og skriv `python setup.py install`
2. Tilslut computeren til Raspberry Pi'ens netværk
3. Åben en terminal i mappen med app.py og skriv `python app.py`
4. Åben en browser og skriv `http://<ip-adresse>:5000/` i adresselinjen eller klik på linket i terminalen

### Mac
1. Åben en terminal i mappen med setup.py og skriv `python setup.py install`
2. Tilslut computeren til Raspberry Pi'ens netværk
3. Åben en terminal i mappen med app.py og skriv `python app.py`
4. Åben en browser og skriv `http://<ip-adresse>:5000/` i adresselinjen eller klik på linket i terminalen

### Linux
1. Åben en terminal i mappen med setup.py og skriv `python setup.py install`
2. Tilslut computeren til Raspberry Pi'ens netværk
3. Åben en terminal i mappen med app.py og skriv `python app.py`
4. Åben en browser og skriv `http://<ip-adresse>:5000/` i adresselinjen eller klik på linket i terminalen

### Hvis du ikke kan finde ip-adressen
1. Åben en terminal og skriv `arp -a`
2. Åben en browser og skriv `http://<ip-adresse>:5000/` i adresselinjen eller klik på linket i terminalen

## Hvis du har problemer med setup.py eller app.py
Kan du prøve at installere de nødvendie pakke manuelt
1. Flask: `pip install flask`
2. Paho: `pip install paho-mqtt`
3. Numpy: `pip install numpy`
4. Json: `pip install json`

