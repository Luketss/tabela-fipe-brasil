import requests


class FipeClient:
    def __init__(self) -> None:
        pass

    def get_request(
        self, endpoint, payload=None, headers=None, params=None, verify=None
    ):
        response = requests.get(
            endpoint, json=payload, headers=headers, params=params, verify=verify
        )
        return response

    def post_request(
        self, endpoint, payload=None, headers=None, params=None, verify=None
    ):
        response = requests.post(
            endpoint, json=payload, headers=headers, params=params, verify=verify
        )
        return response

    def put_request(
        self, endpoint, payload=None, headers=None, params=None, verify=None
    ):
        response = requests.put(
            endpoint, json=payload, headers=headers, params=params, verify=verify
        )
        return response

    def delete_request(
        self, endpoint, payload=None, headers=None, params=None, verify=None
    ):
        response = requests.delete(
            endpoint, json=payload, headers=headers, params=params, verify=verify
        )
        return response
