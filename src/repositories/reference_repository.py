from sqlalchemy import text
from config import db
from entities.reference import Reference


def get_references():
    result = db.session.execute(
        text("SELECT id, author, title, journal, year FROM reference_items"))
    rows = result.fetchall()
    references_list = [
        Reference(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    return references_list


def delete_reference(id):
    sql = text("DELETE FROM reference_items WHERE id=:id")
    db.session.execute(sql, {"id": id})
    db.session.commit()


def create_reference(author, title, journal, year):
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
