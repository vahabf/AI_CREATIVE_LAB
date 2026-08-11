from dataclasses import dataclass


@dataclass
class Lead:
    name: str
    message: str
    budget: str
    deadline: str