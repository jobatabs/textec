from flask import redirect, render_template, request, jsonify, flash, send_file
from sqlalchemy.exc import SQLAlchemyError
from db_helper import reset_db
from repositories.reference_repository import (
    get_references, create_reference, delete_reference, get_title
)
from config import app, test_env
from util import validate_reference, UserInputError
from bib_generator import create_bibfile


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
    pp = request.form.get("pp") if request.form.get("pp") != "" else None

    try:
        validate_reference(author, title, journal, year, pp)
        create_reference(author, title, journal, year, pp)
        flash(f"Successfully added reference {title}.", 'success')
        return redirect("/")
    except UserInputError as error:
        flash(str(error), 'error')
        return redirect("/new")


@app.route("/delete/<reference_id>", methods=["POST"])
def delete(reference_id):
    try:
        title = get_title(reference_id)
        if title:
            delete_reference(reference_id)
            flash(f"Successfully deleted reference {title}.", "success")
        else:
            flash("The reference could not be deleted.", "error")
    except SQLAlchemyError:
        flash("The reference could not be deleted.", "error")
    return redirect("/")


@app.route("/delete/<reference_id>", methods=["GET"])
def handle_get_delete(reference_id):  # pylint: disable=unused-argument
    flash("GET requests are not allowed for deletion.", "error")
    return redirect("/")


@app.route("/export_bibtex_file")
def export_bibtex_file():
    references = get_references()
    create_bibfile(references)

    return send_file("../references.bib", as_attachment=True, download_name="references.bib")


# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
