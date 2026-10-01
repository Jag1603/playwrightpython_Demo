from playwright.sync_api import APIRequestContext


class BaseAPI:

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, endpoint):

        return self.request.get(endpoint)

    def post(self, endpoint, data):

        return self.request.post(
            endpoint,
            data=data
        )
    