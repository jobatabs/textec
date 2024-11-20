# textec
Miniprojekti kurssille TKT20006 Ohjelmistotekniikka
https://ohjelmistotuotanto-hy.github.io/speksi/

- [Product backlog](https://github.com/users/jobatabs/projects/1/views/3)
- [CI](https://github.com/jobatabs/textec/actions)
- [Sprint backlog](https://docs.google.com/spreadsheets/d/1WLDSrKw92wT9KG-hiETiYCesm8fhF46Eo0MnLOWUtcI/edit?gid=0#gid=0)

# Asennusohjeet

1. ``git clone git@github.com:jobatabs/textec.git``
2. ``cd textec``
3. ``pip install poetry``
4. ``poetry install``

# Sovelluksen käynnistäminen

1. ``poetry run python3 src/db_helper.py``
2. ``poetry run python3 src/index.py``

# Testien ajo

1. ``poetry run pytest src/tests``
2. ``poetry run robot src/story_tests``

## Pylint check
[![Pylint](https://github.com/jobatabs/textec/actions/workflows/pylint.yml/badge.svg?branch=mlenni-patch)](https://github.com/jobatabs/textec/actions/workflows/pylint.yml)

# Definition of done

Ollakseen valmis, user storyn toteutuksen tulee olla
- analysoitu (hyväksymiskriteerit kirjattu Robot-testein)
- suunniteltu (jaettu taskeihin)
- ohjelmoitu (huom. autopep8)
- testattu (unittest, Robot läpi)
- testaus automatisoitu (CI passing)
- integroitu muuhun ohjelmistoon ja viety tuotantoympäristöön (main branchissa)
