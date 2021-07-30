import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from app import app
from versions import v1

@app.route("/status", methods=["GET"])
def handshake():
    return jsonify({
        "msg": "Ok, i'm online.",
        "ok": True
    })

if(__name__=="__main__"):
    print("All routes:\n", app.url_map, "\n")
    HOST = os.getenv("HTTP_HOST", "127.0.0.1")
    PORT = os.getenv("HTTP_PORT", 5005)
    DEBUG = os.getenv("DEBUG", False)
    app.run(host=HOST, port=PORT, debug=DEBUG)