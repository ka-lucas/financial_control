from flask_restx import Namespace, fields

# Namespaces
manege_list_ns = Namespace('manege-control')

# Payloads

# adicionar conta, pode estar paga ou nao
add_count_payload = manege_list_ns.model('AddCount', {
    'date': fields.String(required=True),
    'type_payment': fields.String(required=True),
    'value': fields.Float(required=True)
}, strict=True)

# deletar conta
delete_count_payload = manege_list_ns.model('DeleteCountPayload', {
    'count_id': fields.Integer(required=True)
}, strict=True)
