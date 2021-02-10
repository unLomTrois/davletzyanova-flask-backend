from flask import Blueprint, jsonify

api = Blueprint("api", __name__, template_folder="templates")


@api.route("/")
def index():
    return "api"


@api.route("/get_notes")
def get_notes():
    fake_data = [
        {"title": "lol", "description": "lolem ipsum"},
        {"title": "kek", "description": "kekem ipsum"},
    ]
    return jsonify(fake_data)
