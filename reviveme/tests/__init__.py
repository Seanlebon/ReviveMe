import pytest
from reviveme import create_app
from reviveme.db import db

@pytest.fixture()
def app():
    app = create_app(testing=True)

    with app.app_context():
        db.create_all()

    yield app

    # clean up / reset resources here
    with app.app_context():
        db.session.remove()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def app_context(app):
    with app.app_context():
        yield
