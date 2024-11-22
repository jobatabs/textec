from sqlalchemy import text
from config import db
from entities.reference import Reference


def get_references():
    result = db.session.execute(
        text("SELECT id, author, title, journal, year, pp FROM reference_items"))
    rows = result.fetchall()
    references_list = [
        Reference(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
    return references_list


def set_done(id):
    pass
#   db.session.execute(sql, {"id": id})
#   db.session.commit()


def create_reference(author, title, journal, year, pp=None):
    if pp is not None:
        sql = text(
            "INSERT INTO reference_items (author, title, journal, year, pp) "
            "VALUES (:author, :title, :journal, :year, :pp)"
        )
        db.session.execute(sql, {
            "author": author,
            "title": title,
            "journal": journal,
            "year": year,
            "pp": pp
        })
    else:
        sql = text(
            "INSERT INTO reference_items (author, title, journal, year) "
            "VALUES (:author, :title, :journal, :year)"
        )
        db.session.execute(sql, {
            "author": author,
            "title": title,
            "journal": journal,
            "year": year
        })
    
    db.session.commit()
