from flask import Flask
from config.config import SECRET_KEY
from routes.index import index_routes
from routes.upload import upload_routes
from routes.download import download_routes
import logging

logging.basicConfig(filename="web.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

app = Flask(__file__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(index_routes)
app.register_blueprint(upload_routes)
app.register_blueprint(download_routes)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=False)