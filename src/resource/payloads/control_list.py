from flask_restx import Namespace, fields

# Namespaces
control_list_ns = Namespace('control-list')

#Payloads
search_payload = control_list_ns.model('SearchPayload', {
    'start_date': fields.String(required=True),
    'end_date': fields.String(required=True)
}, strict=True)