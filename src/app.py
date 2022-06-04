from flask import Flask


from flask_restx import Api

from src.resource.control_list import GetById, GetAll, GetByDate
from src.resource.manege_account import ManegeList
from src.resource.payloads.control_list import control_list_ns
from src.resource.payloads.manege_account import manege_list_ns
from src.resource.payloads.users import users_ns
from src.resource.users import Users

# configs
app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(manege_list_ns)
api.add_namespace(control_list_ns)
api.add_namespace(users_ns)

# routes
control_list_ns.add_resource(GetById, '/<int:user_id>')
control_list_ns.add_resource(GetAll, '')
control_list_ns.add_resource(GetByDate, '')
manege_list_ns.add_resource(ManegeList, '/<int:user_id>')
users_ns.add_resource(Users, '')
