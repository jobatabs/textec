from sqlalchemy import text
from config import db, app

TABLE_NAME = "reference_items"


def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE TABLE_NAME = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def reset_db():
    print(f"Clearing contents from table {TABLE_NAME}")
    sql = text(f"DELETE FROM {TABLE_NAME}")
    db.session.execute(sql)
    db.session.commit()
    reset_sequence_sql = text(f"ALTER SEQUENCE {TABLE_NAME}_id_seq RESTART WITH 1")
    db.session.execute(reset_sequence_sql)
    db.session.commit()

def setup_db_tests():
    if table_exists(TABLE_NAME):
        print(f"Table {TABLE_NAME} exists, dropping")
        sql = text(f"DROP TABLE {TABLE_NAME}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {TABLE_NAME}")
    sql = text(
        f"CREATE TABLE {TABLE_NAME} ("
        "  id SERIAL PRIMARY KEY,"
        "  author TEXT NOT NULL,"
        "  title TEXT NOT NULL,"
        "  journal TEXT,"
        "  year INTEGER NOT NULL,"
        "  type TEXT NOT NULL,"
        "  pp TEXT,"
        "  volume TEXT,"
        "  number TEXT,"
        "  publisher TEXT,"
        "  howpublished TEXT,"
        "  note TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()


def setup_db():
    if table_exists(TABLE_NAME):
        print(f"Table {TABLE_NAME} exists, dropping")
        sql = text(f"DROP TABLE {TABLE_NAME}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {TABLE_NAME}")
    sql = text(
        f"CREATE TABLE {TABLE_NAME} ("
        "  id SERIAL PRIMARY KEY,"
        "  author TEXT NOT NULL,"
        "  title TEXT NOT NULL,"
        "  journal TEXT,"
        "  year INTEGER NOT NULL,"
        "  type TEXT NOT NULL,"
        "  pp TEXT,"
        "  volume TEXT,"
        "  number TEXT,"
        "  publisher TEXT,"
        "  howpublished TEXT,"
        "  note TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()
    

    db_setup_items = [
        {"author": "Knuth, Donald E", "title": "The Art of Computer Programming, Volume 1: Fundamental Algorithms",
            "year": 1968, "type": "book", "publisher": "Addison-Wesley"},
        {"author": "Tanenbaum, Andrew S., and David J. Wetherall", "title": "Computer Networks",
            "year": 2011, "type": "misc", "howpublished": "Online", "note": "5th ed. Pearson Education"},
        {"author": "Turing, Alan M.", "title": "On Computable Numbers, with an Application to the Entscheidungsproblem", "year": 1937,
            "type": "article", "journal": "Proceedings of the London Mathematical Society", "pp": "230-265", "volume": "s2-42", "number": "1"},
        {"author": "Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein",
            "title": "Introduction to Algorithms", "year": 2022, "type": "book", "publisher": "The MIT Press", "pp": "112-120"},
        {"author": "Shannon, C. E.", "title": "A Mathematical Theory of Communication", "year": 1948, "type": "article",
            "journal": "Bell System Technical Journal", "pp": "379-423", "volume": "27", "number": "3"},
    ]
    for reference in db_setup_items:
        keys = ", ".join(reference.keys())
        values = ", ".join(f":{key}" for key in reference.keys())
        sql = text(f"INSERT INTO {TABLE_NAME} ({keys}) VALUES ({values})")
        db.session.execute(sql, reference)
    db.session.commit()


if __name__ == "__main__": # pragma: no cover
    with app.app_context():
        setup_db()
