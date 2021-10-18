from dataclasses import dataclass
from datetime import datetime


@dataclass(unsafe_hash=True)
class Bookdto:
    id: int
    name: str

