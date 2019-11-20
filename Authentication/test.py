import unittest
import flask_testing

from urllib.request import urlopen
from flask import Flask
from flask_testing import LiveServerTestCase, TestCase

class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)



class TestViews(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app
    def test_some_json(self):
        response = self.client.post("/login",data= {
            "email":"email",
            "password":"password"
        })
        self.assertEquals(response.data, dict(hellow="world"))

if __name__ == '__main__':
    unittest.main()