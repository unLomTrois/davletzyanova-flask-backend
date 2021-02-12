from flask import Blueprint, jsonify, request, make_response
from app.db import Session
from app.db.models import Note
from flask_cors import cross_origin


api = Blueprint("api", __name__, template_folder="templates")


@api.route("/")
def index():
    return "api"


@api.route("/notes", methods=["GET"])
@cross_origin()
def get_notes():
    """Получить все заметки с БД"""

    notes = Session.query(Note).all()

    results = [
        {"id": note.id, "title": note.title, "description": note.description}
        for note in notes
    ]

    return jsonify(results)


@api.route("/notes/<note_id>", methods=["GET"])
@cross_origin()
def get_note(note_id):
    """Получить заметку с индексом из БД"""

    note = Session.query(Note).filter(Note.id == note_id).one()

    result = {"id": note.id, "title": note.title, "description": note.description}

    return jsonify(result)


@api.route("/notes/add", methods=["POST"])
@cross_origin()
def add_note():
    """Добавить новую заметку"""

    response = request.get_json()

    # validation
    if "id" in response and "title" in response and "description" in response:
        try:
            new_note = Note(
                id=response["id"],
                title=response["title"],
                description=response["description"],
            )

            Session.add(new_note)
            Session.commit()

            return make_response(jsonify(success=True), 201)  # Created
        except:
            Session.rollback()
            # raise
            return make_response(jsonify(success=False), 409)  # Conflict
    else:
        return make_response(jsonify(success=False), 400)  # Bad Request


@api.route("/notes/<note_id>/delete", methods=["DELETE"])
@cross_origin()
def delete_note(note_id):
    """Удалить заметку"""

    try:
        Session.query(Note).filter(Note.id == note_id).delete()

        Session.commit()

        return make_response(jsonify(success=True), 200)
    except:
        Session.rollback()

        raise

        return make_response(jsonify(success=True), 404)


@api.route("/notes/<note_id>/update", methods=["PATCH"])
@cross_origin()
def update_note(note_id):
    """Обновить заметку"""

    response = request.get_json()

    try:
        Session.query(Note).filter(Note.id == note_id).update(
            {"title": response["title"], "description": response["description"]}
        )

        Session.commit()

        return make_response(jsonify(success=True), 202)
    except:
        Session.rollback()

        raise

        return make_response(jsonify(success=True), 404)
