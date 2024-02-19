from Login import Login
from client import gd_client


class Loader(Login):
    def __init__(self, client_id):
        super().__init__(client_id)

    @staticmethod
    def load_comments(username):
        user = gd_client.search_user(username)
        return user.get_comments()
