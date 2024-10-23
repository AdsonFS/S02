from pymongo import MongoClient
from pymongo.server_api import ServerApi
from neo4j import GraphDatabase

class Neo4jDriver:
    neo4j_host = "bolt://localhost:7687"
    neo4j_user = "neo4j"
    neo4j_password = "DB2docker"

    driver = None

    staticmethod
    def get_driver():
        if not Neo4jDriver.driver:
            Neo4jDriver.driver = GraphDatabase.driver(Neo4jDriver.neo4j_host, auth=(Neo4jDriver.neo4j_user, Neo4jDriver.neo4j_password))
            Neo4jDriver.driver.execute_query("MATCH(n) DETACH DELETE n")
        return Neo4jDriver.driver

class Player:
    def __init__(self, id, name):
        self.name = name
        self.id = id

class Match:
    def __init__(self, id, players, winner):
        self.id = id
        self.players = players
        self.winner = winner


class PlayerDAO:
    def __init__(self) -> None:
        self.neo4j_driver = Neo4jDriver.get_driver()

    def create_player(self, player: Player):
        query = """
        CREATE (p:Player {id: $id, name: $name})
        """
        with self.neo4j_driver.session() as session:
            session.run(query, id=player.id, name=player.name)

    def update_player(self, player: Player):
        query = """
        MATCH (p:Player {id: $id})
        SET p.name = $name
        """
        with self.neo4j_driver.session() as session:
            session.run(query, id=player.id, name=player.name)

    def delete_player(self, player_id: str):
        query = """
        MATCH (p:Player {id: $player_id})
        DETACH DELETE p
        """
        with self.neo4j_driver.session() as session:
            session.run(query, player_id=player_id)

    def get_player(self, player_id: str):
        query = """
        MATCH (p:Player {id: $player_id})
        RETURN p.id AS id, p.name AS name
        """
        with self.neo4j_driver.session() as session:
            result = session.run(query, player_id=player_id)
            return result.single()

    def list_players(self):
        query = """
        MATCH (p:Player)
        RETURN p.id AS id, p.name AS name
        """
        with self.neo4j_driver.session() as session:
            result = session.run(query)
            return result.data()


class MatchDAO:
    def __init__(self) -> None:
        self.neo4j_driver = Neo4jDriver.get_driver()

    def create_match(self, match: Match):
        query = """
        CREATE (m:Match {id: $id, winner: $winner})
        WITH m
        UNWIND $players AS playerId
        MATCH (p:Player {id: playerId})
        CREATE (p)-[:PARTICIPATED_IN]->(m)
        """
        with self.neo4j_driver.session() as session:
            session.run(query, id=match.id, winner=match.winner, players=match.players)

    def get_match(self, match_id: str):
        query = """
        MATCH (m:Match {id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
        RETURN m.id AS id, m.winner AS winner, collect(p.id) AS players
        """
        with self.neo4j_driver.session() as session:
            result = session.run(query, match_id=match_id)
            return result.single()

    def get_player_history(self, player_id: str):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS match_id, m.winner AS winner
        """
        with self.neo4j_driver.session() as session:
            result = session.run(query, player_id=player_id)
            return result.data()

player_dao = PlayerDAO()
match_dao = MatchDAO()

