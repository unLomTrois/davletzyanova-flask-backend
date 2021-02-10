import os
from flask import Flask, send_from_directory
from app.api import api

app = Flask(__name__, static_folder='public')

# register api
app.register_blueprint(api, url_prefix="/api")

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
