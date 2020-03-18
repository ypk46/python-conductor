import json
import requests
from conductor.helper import HttpHelper


class ConductorManager:
    def __init__(self, server: str = "http://localhost:8080/api"):
        self.server = server

    def poll_task(self, task: str, worker_id: str):
        url = "{0}/tasks/poll/{1}".format(self.server, task)
        params = {}
        params["workerid"] = worker_id

        try:
            resp = requests.get(url, params=params)
            HttpHelper.check_request(resp)
            if resp.content == b"":
                return None
            return resp.json()
        except Exception as err:
            print("Error while polling task: " + str(err))
            return None

    def update_task(self, task_payload: dict):
        url = "{0}/tasks".format(self.server)
        headers = {"Accept": "text/plain", "Content-Type": "application/json"}
        json_payload = json.dumps(task_payload, ensure_ascii=False)

        try:
            resp = requests.post(url, data=json_payload, headers=headers)
            HttpHelper.check_request(resp)
        except Exception as err:
            print("Error while updating task: " + str(err))
            return None
