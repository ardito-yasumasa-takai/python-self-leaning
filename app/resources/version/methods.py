from flask_restplus import fields, Resource, Namespace
from http import HTTPStatus
from app.utils.validation import validate, ValidationUtil
from .validators import validate_sample_get_request

# from app.modules.db_connection import db_connection
from app.models import BadRequestResponseModel
import time


api = Namespace("version", description="サンプル")


@api.route('')
class VersionResouce(Resource):
    """ さしすせそ. たちつてと."""

    @validate(validate_sample_get_request)
    @api.response(
        code=HTTPStatus.BAD_REQUEST,
        description="Bad Request",
        model=BadRequestResponseModel(api).badrequest_response_model())
    @api.response(code=HTTPStatus.UNAUTHORIZED, description="Unauthorized")
    @api.response(code=HTTPStatus.FORBIDDEN, description="Forbidden")
    @api.response(code=HTTPStatus.NOT_FOUND, description="Resource not found")
    def get(self):
        """ Sample 取得. """
        return {
            'version': '0.0.1'
        }