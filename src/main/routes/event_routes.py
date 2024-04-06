from flask import Blueprint, jsonify, request

from src.data.event_handler import EventHandler
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest

event_routes_bp = Blueprint("event_route", __name__)


@event_routes_bp.route("/events", methods=["POST"])
def create_event():
    try:
        handler = EventHandler()
        http_request = HttpRequest(body=request.json)

        http_response = handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@event_routes_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        handler = EventHandler()
        http_request = HttpRequest(param={"event_id": event_id})

        http_response = handler.find_by_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
