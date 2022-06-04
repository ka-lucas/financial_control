from src.util.file import get_data, insert_data
import random

db_name = 'accounts.json'


class ManegeAccountCore:
    def list_payments(self, user_id):
        accounts = get_data(db_name)
        accounts_names = [account['name'] for account in accounts if user_id == account['user_id']]
        return accounts_names

    def add_accounts(self, data, user_id):
        data['_id'] = random.randint(1, 9999999999)
        data['user_id'] = user_id
        accounts = get_data(db_name)
        accounts.append(data)
        insert_data(accounts, db_name)
        return accounts

    def delete_accounts(self, data, user_id):
        accounts = get_data(db_name)
        for index, count in enumerate(accounts):
            if data['_id'] == count['_id'] and user_id == count['user_id']:
                del (accounts[index])
        insert_data(accounts, db_name)
        return accounts
