from flask import Blueprint, request
from controllers.DownloadController import DownloadController

download_routes = Blueprint('download_routes', __name__, url_prefix="/")

@download_routes.route("/download/<archive_name>", methods=["GET"])
def download_archive(archive_name):
    if request.method == "GET":
        return DownloadController().send_pdf_file(request, archive_name)