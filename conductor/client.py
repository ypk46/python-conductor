import time
import socket
from typing import Callable
from conductor.manager import ConductorManager


class ConductorClient:
    def __init__(self, server: str, polling_interval: int, worker_id: str = None):
        """
        Parameters
        ----------
        server: str
            The url to conductor API.
            Ex: 'http://localhost:8080/api'
        polling_interval: int
            Number of milliseconds the client will wait between task polls.
        worker_id: str, optional
            The id of the worker executing the tasks
        """
        self.manager = ConductorManager(server)
        self.polling_interval = polling_interval
        self.worker_id = worker_id if worker_id else socket.gethostname()

    def start(self, task: str, exec_function: Callable):
        """
        Parameters
        ----------
        task: str
            Name of the task to be polled.
        exec_function: Callable
            Function that will be executed on pending tasks arrival
        """
        print("Polling '{0}' at {1} ms interval!".format(task, self.polling_interval))
        while True:
            time.sleep(float(self.polling_interval / 1000))
            polled = self.manager.poll_task(task, self.worker_id)
            if polled is not None:
                self.execute(polled, exec_function)

    def execute(self, task: str, exec_function: Callable):
        try:
            resp = exec_function(task)
            if type(resp) is not dict or not all(
                key in resp for key in ("status", "output", "logs")
            ):
                raise Exception(
                    "Task execution function MUST return a response as a dict"
                    " with status, output and logs fields"
                )

            payload = {}
            payload["taskId"] = task["taskId"]
            payload["workflowInstanceId"] = task["workflowInstanceId"]

            payload["logs"] = resp["logs"]
            payload["status"] = resp["status"]
            payload["outputData"] = resp["output"]

            if "reasonForIncompletion" in resp:
                payload["reasonForIncompletion"] = resp["reasonForIncompletion"]

            self.manager.update_task(payload)
        except Exception as err:
            print("Error executing task: " + str(err))
            payload["status"] = "FAILED"
            self.manager.update_task(payload)
