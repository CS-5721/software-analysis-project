from http import HTTPStatus
from django.test import TestCase
from housemate.forms import registerForm
import django.db

django.db.connection.creation.create_test_db # in memory db

class RegisterFormTests(TestCase):
    def test_get(self):
        response = self.client.get("/housemate/register")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        #self.assertContains(response, "<h1>html for the page</h1>", html=True)

    def test_post_success(self):
        response = self.client.post(
            "/housemate/register", data={"user":"","password": "Login@123","password2": "Login@123","email":""}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        # This route does not redirect...
        #self.assertEqual(response.status_code, HTTPStatus.FOUND)
        #self.assertEqual(response["password2"], "/registration/register_done.html")

    def test_post_error(self):
        response = self.client.post(
            "/housemate/register", data={"password": "Login@123","password2": "Login2222"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Passwords don't match.", html=True
        )

