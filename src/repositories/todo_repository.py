from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_todos():
    # result = db.session.execute(text("SELECT id, content, done FROM todos"))
    # todos = result.fetchall()
    # return [Todo(todo[0], todo[1], todo[2]) for todo in todos] 
    pass

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

