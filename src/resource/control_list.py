from flask import request
from flask_restx import Resource

from src.core.control_list import *
from src.resource.payloads.control_list import *


class GetAll(Resource):
    def get(self):
        get_all_core = GetAllCore()
        result = get_all_core.search()
        return result


class GetByDate(Resource):
    @control_list_ns.expect(search_payload, validate=True)
    def post(self):
        data = request.get_json()
        get_by_date_core = GetByDateCore()
        result = get_by_date_core.search(data)
        return result


class GetById(Resource):
    def get(self, user_id):
        get_by_id_core = GetByIdCore()
        result = get_by_id_core.search(user_id)
        return result
