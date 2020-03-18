from conductor import ConductorClient


def action(task: dict):
    return {
        "status": "COMPLETED",
        "output": {"result": 0},
        "logs": [{"message": "Task completed successfully"}],
    }


def main():
    client = ConductorClient("http://localhost:8080/api", 1000)
    client.start("action", action)


if __name__ == "__main__":
    main()
