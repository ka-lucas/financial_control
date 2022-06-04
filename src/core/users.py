from src.util.file import insert_data, get_data

db_name = 'users.json'


class UsersCore:
    def list_users(self):
        all_users = get_data(db_name)
        users_name = []
        for user in all_users:
            users_name.append(user['nome'])
        return users_name

    def create_user(self, data):
        all_users = get_data(db_name)
        all_users.append(data)
        insert_data(all_users, db_name)
        return all_users

    def update_user(self, data):
        all_users = get_data(db_name)
        for index, user in enumerate(all_users):
            if data['_id'] == user['_id']:
                all_users[index] = data
        insert_data(all_users, db_name)
        return all_users

    def remove_user(self, data):
        all_users = get_data(db_name)
        for index, user in enumerate(all_users):
            if data['_id'] == user['_id']:
                del (all_users[index])
        insert_data(all_users, db_name)
        return all_users
