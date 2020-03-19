# Python Conductor (Mini client for Conductor)

This a simple python wrapper for Netflix Conductor task polling and task update.

## Installation

    pip install python-conductor

## Using Conductor Client

```python
from conductor import ConductorClient

def action(task: dict):
    # do some fancy operation

client = ConductorClient("http://localhost:8080/api", 1000)
client.start("action", action)
```

## Using Conductor Manager

```python
from conductor import ConductorManager

manager = ConductorManager("http://localhost:8080/api")
```
