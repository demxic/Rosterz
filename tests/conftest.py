import pytest

from app import create_app
from flask_settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    """As this fixture has been defined with a scope of a function, it will be recreated for each test because
        we do not want to reuse the application that another test has already tainted"""
    return create_app(TestConfig)
