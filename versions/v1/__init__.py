version_name = "v1"

from flask.json import jsonify
from .routes import auth, product, order

from app import app

@app.route(f"/{version_name}/status", methods=["GET", "POST"])
def status():
    return jsonify({
        "msg": f"Version {version_name}.",
        "ok": True
    })