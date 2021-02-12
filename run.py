from app import app
from os import environ


if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))

    app.run(use_reloader=True, port=port, threaded=True)