from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

class GomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>To-Do</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))