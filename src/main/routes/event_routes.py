from flask import Blueprint, jsonify, request

from src.data.event_handler import EventHandler
from src.http_types.http_request import HttpRequest

event_routes_bp = Blueprint("event_route", __name__)


@event_routes_bp.route("/events", methods=["POST"])
def create_event():
    http_request = HttpRequest(body=request.json)
    handler = EventHandler()
    http_response = handler.register(http_request)
    return jsonify(http_response.body), http_response.status_code