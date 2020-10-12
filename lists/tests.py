from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # 检查网站根路径‘/'，能否找到名为home_page的函数
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() # 创建一个HTTPRequest对象
        response = home_page(request) # 传给home_page视图，得到响应
        html = response.content.decode('utf8') # 提取content，得到原始字节
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
