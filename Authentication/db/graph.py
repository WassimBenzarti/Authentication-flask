import os
from neo4j import GraphDatabase


class Neo4jDatabase:

    def __init__(self):
        self._driver = GraphDatabase.driver(os.getenv("DB_URI"), auth=(os.getenv("DB_USER"), os.getenv("DB_PASS")))

    def query(self,*args, **kwargs):
        with self._driver.session() as session:
            return session.run(*args,**kwargs)

    def close(self):
        self._driver.close()

    @staticmethod
    def getInstance():
        return Neo4jDatabase()