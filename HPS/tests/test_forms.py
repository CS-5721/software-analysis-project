from http import HTTPStatus
from django.test import TestCase
from housemate.forms import LoginForm
from housemate.models import User as UserModel
import django.db

django.db.connection.creation.create_test_db # in memory db

class TestLoginForm(TestCase):
    def test_valid_form(self):
        w = UserModel.objects.create(username="anyuser",
                                    email="test@test.com",
                                    phone="9999999999",
                                    password="123456")
        data = {'username': w.username, 'password': w.password, }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = UserModel.objects.create(username="",
                                     email="test@test.com",
                                     phone="9999999999",
                                     password="")
        data = {'username': w.username, 'password': w.password, }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

