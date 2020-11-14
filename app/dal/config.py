from dataclasses import dataclass
import os


@dataclass
class Config:
    url = 'neo4j://db:7687'
    username = os.environ.get('NEO4J_USER', 'username')
    password = os.environ.get('NEO4J_PASS', 'password')
