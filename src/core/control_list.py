from src.util.file import get_data

db_name = "accounts.json"


class GetAllCore:
    def search(self):
        return get_data(db_name)


class GetByDateCore:
    def search(self, data):
        accounts = get_data(db_name)
        return [account['value'] for account in accounts if data['start_date'] < account['date'] < data['end_date']]


class GetByIdCore:
    def search(self, user_id):
        accounts = get_data(db_name)
        return [account['value'] for account in accounts if user_id == account['user_id']]
