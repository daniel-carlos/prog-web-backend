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
    print("\n\n", app.url_map, "\n\n")
    app.run(host="127.0.0.1", port=5005, debug=True)