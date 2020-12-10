from http import HTTPStatus
from django.test import TestCase
from housemate.forms import registerForm


class RegisterFormTests(TestCase):
    def test_get(self):
        response = self.client.get("/registration/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        #self.assertContains(response, "<h1>html for the page</h1>", html=True)

    def test_post_success(self):
        response = self.client.post(
            "/registration/", data={"user":"","password": "Login@123","password2": "Login@123","email":""}
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["password2"], "/registration/register_done.html")

    def test_post_error(self):
        response = self.client.post(
            "/registration//", data={"password": "Login@123","password2": "Login2222"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Passwords don't match.", html=True
        )

