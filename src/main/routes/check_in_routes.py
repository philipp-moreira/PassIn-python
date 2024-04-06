from flask import Blueprint, jsonify
from src.data.check_in_handler import CheckInHandler
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest

check_in_route_bp = Blueprint("check_in_routes", __name__)


@check_in_route_bp.route("/checkins/<attendee_id>", methods=["POST"])
def create_check_in(attendee_id):
    try:
        handler = CheckInHandler()
        http_request = HttpRequest(param={"attendee_id": attendee_id})

        http_response = handler.registry(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
