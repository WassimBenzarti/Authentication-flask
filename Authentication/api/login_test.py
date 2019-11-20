import os
import tempfile

import unittest

from flask.testing import FlaskClient

from login import app

client = FlaskClient(app)


res = client.post("/login",data= {
    "email":"email@mail.com",
    "password":"123"
})
print(res)


