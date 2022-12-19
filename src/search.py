from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.static.STATIONS import STATIONS

bp = Blueprint("search", __name__)


def search_route():
    pass


@bp.route("/search", methods=["POST", "GET"])
def home():
    stations = STATIONS
    if request.method == "POST":
        start_station = request.form["start_station"]
        end_station = request.form["end_station"]
        error = None

        if not start_station:
            error = "Missing Start"
        if not end_station:
            error = "Missing End"

        if error is not None:
            flash(error)
        else:
            search_route()

    return render_template("search/search.html", stations=stations)
