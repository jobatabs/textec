from config import db
from sqlalchemy import text

from entities.citation import Citation

def get_citations():
    result = db.session.execute(text("SELECT id, author, title, journal, year FROM citations"))
    rows = result.fetchall()
    citations_list = [Citation(row[0], row[1], row[2], row[3], row[4]) for row in rows]
    return citations_list

def set_done(todo_id):
    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": todo_id })
    db.session.commit()

def create_reference(author, title, journal, year):
    sql = text("INSERT INTO citations (author, title, journal, year) VALUES (:author, :title, :journal, :year)")
    db.session.execute(sql, {
        "author": author,
        "title": title,
        "journal": journal,
        "year": year
    })
    db.session.commit()

