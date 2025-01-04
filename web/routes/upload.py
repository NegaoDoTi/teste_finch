from flask import Blueprint, request
from controllers.UploadController import UploadController

upload_routes = Blueprint("upload_routes", __name__, url_prefix="/")

@upload_routes.route("/upload/pdfs", methods=["POST"])
def uploads_pdf():
    if request.method == "POST":
        return UploadController().uploaded_pdfs_files(request)