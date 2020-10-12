from django.test import TestCase

# Create your tests here.
from django.urls import resolve

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # 检查网站根路径‘/'，能否找到名为home_page的函数
        self.assertEqual(found.func, home_page)