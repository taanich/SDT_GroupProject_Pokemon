from app.db.graph import run_query

def get_all_nodes(limit: int = 10):
    cypher = """
    MATCH (n)
    RETURN n
    LIMIT $limit
    """
    return run_query(cypher, {"limit": limit})


def get_books():
    """Example for your current database content."""
    cypher = """
    MATCH (b:Book)
    RETURN b
    LIMIT 25
    """
    return run_query(cypher)