#!venv/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import User


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_changePassword(self):
        u = User(username='toto')
        u.set_password('bla')
        self.assertFalse(u.check_password('bli'))
        self.assertTrue(u.check_password('bla'))

if __name__ == '__main__':
    unittest.main()