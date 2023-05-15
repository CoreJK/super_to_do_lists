from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """测试 `/` RUL路由是否正常解析到 home_page 函数上"""
        found = resolve('/home_page/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """测试 home_page 视图是否返回符合条件的内容"""
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

