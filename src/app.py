from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference, set_done
from config import app, test_env
from util import validate_reference, UserInputError


@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/create", methods=["POST"])
def creation():
    author = request.form.get("author")
    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")

    try:
        validate_reference(author, title, journal, year)
        create_reference(author, title, journal, year)
        flash(f"Successfully added reference {title}.", 'success')
        return redirect("/")
    except UserInputError as error:
        flash(str(error), 'error')
        return redirect("/new")


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
