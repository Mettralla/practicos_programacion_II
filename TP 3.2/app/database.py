import mysql.connector

class DatabaseConnection:
    _connections = {}

    @classmethod
    def get_connection(cls, db: str):
        if db not in cls._connections:
            cls._connections[db] = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                port="3306",
                password="0deGxGVAqooB#",
                database=db
            )
        return cls._connections[db]

    @classmethod
    def execute_query(cls, db, query, params=None):
        connection = cls.get_connection(db)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()

    @classmethod
    def fetch_one(cls, db, query, params=None):
        connection = cls.get_connection(db)
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    @classmethod
    def fetch_all(cls, db, query, params=None):
        connection = cls.get_connection(db)
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    @classmethod
    def close_connections(cls):
        for connection in cls._connections.values():
            connection.close()
        cls._connections = {}
