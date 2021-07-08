from . import bp

@bp.route("/route_name", methods=["GET"])
def route_name():
    return "Example of route."