from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference
from config import app, test_env
from util import validate_reference


@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", todos=references)


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
        validate_reference(year)
        create_reference(author, title, journal, year)
        flash(f"Successfully added reference {title}.", 'success')
        return redirect("/")
    except Exception as error:
        flash(str(error), 'error')
        return redirect("/new_todo")


@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
