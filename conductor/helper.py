import requests


class HttpHelper:
    @staticmethod
    def check_request(resp):
        try:
            resp.raise_for_status()
        except requests.HTTPError:
            print("ERROR: " + resp.text)
            raise

    @staticmethod
    def parse_response(resp, header):
        parsed = ""
        if len(resp.text) > 0:
            if header["Accept"] == "text/plain":
                parsed = resp.text
            elif header["Accept"] == "application/json":
                parsed = resp.json()
            else:
                parsed = resp.text
        return parsed
