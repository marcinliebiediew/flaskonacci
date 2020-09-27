from src.models import Logs


def test_config(config):
    assert config['SQLALCHEMY_DATABASE_URI']


def test_connection(db):
    assert db.engine.execute("SELECT 1 FROM logs")
