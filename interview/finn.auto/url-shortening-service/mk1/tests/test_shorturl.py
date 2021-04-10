import os
import tempfile

import pytest

import shorturl


@pytest.fixture
def client():
    db_fd, shorturl.app.config['DATABASE'] = tempfile.mkstemp()
    shorturl.app.config['TESTING'] = True

    with shorturl.app.test_client() as client:
        with shorturl.app.app_context():
            shorturl.init_db()
        yield client

    os.close(db_fd)
    os.unlink(shorturl.app.config['DATABASE'])


def test_encode():
    assert True
