from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

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
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        """测试 home_page 函数能否处理 POST 表单请求"""
        # 设置配置，前置条件
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        # 执行代码
        response = home_page(request)

        # 编写断言
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)

