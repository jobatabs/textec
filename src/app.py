from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, create_reference, set_done
from config import app, test_env
from util import validate_todo

@app.route("/")
def index():
    return render_template("index.html") 

    # todos = get_todos()
    # unfinished = len([todo for todo in todos if not todo.done])
    # return render_template("index.html" , todos=todos, unfinished=unfinished) 

@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")

    try:
        validate_todo(year)
        create_reference(author, title, journal, year)
        flash(f"Successfully added reference {title}.", 'success')
        return redirect("/")
    except Exception as error:
        flash(str(error), 'error')
        return  redirect("/new_todo")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
