from flask import Blueprint, request
from controllers.IndexController import IndexController
from pathlib import Path

index_routes = Blueprint("index_routes", __name__, template_folder="templates", url_prefix="/")

@index_routes.route("", methods=["GET"])
def index():
    if request.method == "GET":
        return IndexController().index()