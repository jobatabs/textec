# textec
Miniprojekti kurssille TKT20006 Ohjelmistotekniikka
https://ohjelmistotuotanto-hy.github.io/speksi/

- [Product backlog](https://github.com/users/jobatabs/projects/1/views/3)
- [CI](https://github.com/jobatabs/textec/actions)

# Asennusohjeet

1. ``git clone git@github:jobatabs/textec``
2. ``cd textec``
3. ``pip install poetry``
4. ``poetry install``

# Sovelluksen käynnistäminen

1. ``poetry run python3 src/db_helper.py``
2. ``poetry run python3 src/index.py``

# Testien ajo

1. ``poetry run pytest src/tests``
2. ``poetry run robot src/story_tests``

# Definition of done

Ollakseen valmis, user storyn toteutuksen tulee olla
- analysoitu (hyväksymiskriteerit kirjattu)
- suunniteltu (jaettu taskeihin)
- ohjelmoitu (huom. autopep8)
- testattu (unittest, Robot)
- testaus automatisoitu (unittest, Robot, pylint)
- integroitu muuhun ohjelmistoon ja viety tuotantoympäristöön (main branchissa)
