from sqlalchemy import text
from config import db
from entities.reference import Reference


def get_references():
    result = db.session.execute(
        text("SELECT id, author, title, journal, year, type, pp, volume, number, publisher, howpublished, note FROM reference_items"))
    rows = result.fetchall()
    references_list = [
        Reference(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]) for row in rows] #otetaanko kaikki?
    return references_list


def delete_reference(_id):
    sql = text("DELETE FROM reference_items WHERE id=:id")
    db.session.execute(sql, {"id": _id})
    db.session.commit()


def create_reference(references:dict): #toimiiko???
    filtered_references = {key: value for key, value in references.items() if value is not None}

    keys = ", ".join(filtered_references.keys())
    values = ", ".join(f":{key}" for key in filtered_references.keys())
    
    sql = text(f"INSERT INTO reference_items ({keys}) VALUES ({values})")

    db.session.execute(sql, filtered_references)
    db.session.commit()


    # if pp is not None:
    #     sql = text(
    #         "INSERT INTO reference_items (author, title, journal, year, type, pp, volume, number, publisher, howpublished, note) "
    #         "VALUES (:author, :title, :journal, :year, :type, :pp, :volume, :number, :publisher, :howpublished, :note)"
    #     )
    #     db.session.execute(sql, {
    #         "author": author,
    #         "title": title,
    #         "journal": journal,
    #         "year": year,
    #         "type": type
    #         "pp": pp,
    #         "volume": volume,
    #         "number": number,
    #         "publisher": publisher,
    #         "howpublished": howpublished,
    #         "note": note
    #     })
    # else:
    #     sql = text(
    #         "INSERT INTO reference_items (author, title, journal, year) "
    #         "VALUES (:author, :title, :journal, :year)"
    #     )
    #     db.session.execute(sql, {
    #         "author": author,
    #         "title": title,
    #         "journal": journal,
    #         "year": year
    #     })

    # db.session.commit()


def get_title(_id):
    sql = text("SELECT title FROM reference_items WHERE id = :id")
    result = db.session.execute(sql, {"id": _id}).fetchone()
    if result:
        return result[0]
    return None
