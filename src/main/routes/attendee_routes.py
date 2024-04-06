from flask import Blueprint, jsonify, request
from src.data.attendee_handler import AttendeeHandler
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest


attendee_routes_bp = Blueprint("attendee_route", __name__)


@attendee_routes_bp.route("/attendees/<event_id>/register", methods=["POST"])
def create_attendee(event_id):
    try:
        handler = AttendeeHandler()
        http_request = HttpRequest(body=request.json, param={"event_id": event_id})

        http_response = handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendee_routes_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_badge(attendee_id):
    try:
        handler = AttendeeHandler()
        http_request = HttpRequest(param={"attendee_id": attendee_id})

        http_response = handler.find_attendee_badge(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendee_routes_bp.route("/attendees/<event_id>/attendees", methods=["GET"])
def get_attendees_by_event_id(event_id):
    try:
        handler = AttendeeHandler()
        http_request = HttpRequest(param={"event_id": event_id})

        http_response = handler.find_attendees_by_event_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
