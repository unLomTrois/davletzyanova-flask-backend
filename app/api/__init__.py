from flask import Blueprint, render_template, abort

api = Blueprint("api", __name__, template_folder="templates")


@api.route("/")
def index():
    return "api"
