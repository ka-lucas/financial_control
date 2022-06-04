from flask import request
from flask_restx import Resource

from src.core.manege_account import ManegeAccountCore
from src.resource.payloads.manege_account import *

manege_list_core = ManegeAccountCore()


class ManegeList(Resource):
    @manege_list_ns.expect(add_count_payload, validate=True)
    def put(self, user_id):
        data = request.get_json()
        result = manege_list_core.add_accounts(data, user_id)
        return result

    @manege_list_ns.expect(delete_count_payload, validate=True)
    def delete(self, user_id):
        data = request.get_json()
        result = manege_list_core.delete_accounts(data, user_id)
        return result
