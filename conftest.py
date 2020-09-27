import os
import pathlib

import pytest

from src.app import create_app
from src.extensions import db as _db


@pytest.fixture
def app():
    CONFIG_PATH = os.path.join(
        pathlib.Path(__file__).parent.absolute(), 'application_test.cfg')
    app = create_app(CONFIG_PATH)

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    return app


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c


@pytest.fixture
def db(app):
    TESTDB_PATH = os.path.join(
        pathlib.Path(__file__).parent.absolute(),
        app.config['SQLALCHEMY_DATABASE_URI'].split('/')[-1])

    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    print(TESTDB_PATH)

    def teardown():
        db.drop_all()
        pathlib.Path.unlink(TESTDB_PATH)
        os.remove(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    return _db
