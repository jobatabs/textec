# textec
[![CI](https://github.com/jobatabs/textec/actions/workflows/ci.yaml/badge.svg)](https://github.com/jobatabs/textec/actions/workflows/ci.yaml)
[![CodeQL](https://github.com/jobatabs/textec/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/jobatabs/textec/actions/workflows/github-code-scanning/codeql)
[![Pylint](https://github.com/jobatabs/textec/actions/workflows/pylint.yml/badge.svg)](https://github.com/jobatabs/textec/actions/workflows/pylint.yml)
[![codecov](https://codecov.io/gh/jobatabs/textec/graph/badge.svg?token=45NHI95DUL)](https://codecov.io/gh/jobatabs/textec)

Miniprojekti kurssille TKT20006 Ohjelmistotekniikka
https://ohjelmistotuotanto-hy.github.io/speksi/

- [Product backlog](https://github.com/users/jobatabs/projects/1/views/3)
- [CI](https://github.com/jobatabs/textec/actions)
- [Sprint backlog](https://docs.google.com/spreadsheets/d/1WLDSrKw92wT9KG-hiETiYCesm8fhF46Eo0MnLOWUtcI/edit?gid=0#gid=0)
- [Testikattavuus](https://codecov.io/gh/jobatabs/textec)

# Asennusohjeet

1. ``git clone git@github.com:jobatabs/textec.git``
2. ``cd textec``
3. ``pip install poetry``
4. ``poetry install``

# .env tiedoston luominen

Sovellus käyttää PostgreSQL-tietokantaa, ja sen käynnistämiseksi tarvitaan `.env`-tiedosto, joka sisältää seuraavat ympäristömuuttujat: 

```env 
DATABASE_URL=postgresql://xxx
TEST_ENV=true
SECRET_KEY=satunnainen_merkkijono
```

# Sovelluksen käynnistäminen

1. ``poetry run python3 src/db_helper.py``
2. ``poetry run python3 src/index.py``

# Testien ajo

1. ``poetry run pytest src/tests``
2. ``poetry run robot src/story_tests``

# Definition of done

Ollakseen valmis, user storyn toteutuksen tulee olla
- analysoitu (hyväksymiskriteerit kirjattu Robot-testein)
- suunniteltu (jaettu taskeihin)
- ohjelmoitu (huom. autopep8)
- testattu (unittest, Robot läpi)
- testaus automatisoitu (CI passing)
- integroitu muuhun ohjelmistoon ja viety tuotantoympäristöön (main branchissa)

# Hyväksymiskriteerit

[Käyttäjä voi lisätä 3 eri tyyppistä lähdettä](https://github.com/jobatabs/textec/blob/main/src/story_tests/add_reference.robot)

[Käyttäjä voi muokata lisättyä lähdettä](https://github.com/jobatabs/textec/blob/main/src/story_tests/edit_reference.robot)



