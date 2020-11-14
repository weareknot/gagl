import os


host = os.environ.get('NEO4J_HOST', 'db')
port = os.environ.get('NEO4J_PORT', 7687)
username = os.environ.get('NEO4J_USER', 'username')
password = os.environ.get('NEO4J_PASS', 'password')
url = f'bolt://{username}:{password}@{host}:{port}'
