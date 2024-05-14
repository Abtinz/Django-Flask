import psycopg2

class PostgresService():
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            
        )