import app
import unittest


class AppTest(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_open_accept_get(self):
        header = {
            "Accept": "*/*"
        }
        result = self.app.get(
            "/",
            headers=header
        )
        assert result.data == b"<p>Hello World!</p>"

    def test_open_accept_post(self):
        header = {
            "Accept": "*/*"
        }
        result = self.app.post(
            "/",
            headers=header
        )
        assert result.data == b"<p>Hello World!</p>"

    def test_html_get(self):
        header = {
            "Accept": "text/html"
        }
        result = self.app.get(
            "/",
            headers=header
        )
        assert result.data == b"<p>Hello World!</p>"

    def test_html_post(self):
        header = {
            "Accept": "text/html"
        }
        result = self.app.post(
            "/",
            headers=header
        )
        assert result.data == b"<p>Hello World!</p>"

    def test_json_get(self):
        header = {
            "Accept": "application/json"
        }
        result = self.app.get(
            "/",
            headers=header
        )
        assert result.data == b'{"message":"Good morning"}\n'

    def test_json_post(self):
        header = {
            "Accept": "application/json"
        }
        result = self.app.post(
            "/",
            headers=header
        )
        assert result.data == b'{"message":"Good morning"}\n'
