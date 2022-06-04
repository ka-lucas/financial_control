from flask import request
from flask_restx import Resource

from src.core.users import UsersCore
from src.resource.payloads.users import delete_payload, create_payload, users_ns

users_core = UsersCore()


class Users(Resource):
    def get(self):
        result = users_core.list_users()
        return result

    @users_ns.expect(create_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = users_core.create_user(data)
        return result

    @users_ns.expect(create_payload, validate=True)
    def put(self):
        data = request.get_json()
        result = users_core.update_user(data)
        return result

    @users_ns.expect(delete_payload, validate=True)
    def delete(self):
        data = request.get_json()
        result = users_core.remove_user(data)
        return result
