# Python Conductor (Mini client for Conductor)

This a simple python wrapper for Netflix Conductor task polling and task update.

## Installation

    pip install python-conductor

## Using Conductor Client

```python
from conductor import ConductorClient

client = ConductorClient("http://localhost:8080/api", 1000)
client.start("action", action)
```
