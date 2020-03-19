from conductor import ConductorClient
from conductor import ConductorManager


# Conductor Client Example (Used for task polling and handling method execution)
def action(task: dict):
    return {
        "status": "COMPLETED",
        "output": {"result": 0},
        "logs": [{"message": "Task completed successfully"}],
    }


def main():
    client = ConductorClient("http://localhost:8080/api", 1000)
    client.start("action", action)


# Conductor Manager Example (Used to interact with Conductor API)
def manage():
    manager = ConductorManager("http://localhost:8080/api")
    update_payload = {}
    manager.update_task(update_payload)


if __name__ == "__main__":
    main()
