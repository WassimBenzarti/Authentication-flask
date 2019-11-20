import unittest
from unittest import TestCase
from login import app

class LoginTest(TestCase):

    def test_index(self):
        tester = app.test_client()
        response = tester.post("/login", json={
            "email":"wass11121996@gmail.com",
            "password": "123"
        })
        self.assertEqual(response.status_code, 200)

